import aiohttp
import aiofiles
import asyncio
from datetime import datetime, timedelta
import glob
import os
from time import time

from .state import State
from logger import logger, log_exception
from utils import CtmConverter, textgrid_to_utterance


class Manager:
    def __init__(
        self,
        TICK_INTERVAL: int,
        DATA_DIR: str,
        SUBJECT_MAPPING_PATH: str,
        MY_SECTIONS_PATH: str,
        STATE_PATH: str,
        SERVER_URL_BASE: str,
        DOWNLOAD_FAIL_TIMEOUT_SECS: float,
    ):
        self.TICK_INTERVAL = TICK_INTERVAL
        self.DATA_DIR = DATA_DIR
        self.SUBJECT_MAPPING_PATH = SUBJECT_MAPPING_PATH
        self.MY_SECTIONS_PATH = MY_SECTIONS_PATH
        self.STATE_PATH = STATE_PATH
        self.SERVER_URL_BASE = SERVER_URL_BASE
        self.DOWNLOAD_FAIL_TIMEOUT_SECS = DOWNLOAD_FAIL_TIMEOUT_SECS

        # Paths to data directories.
        self.dir_01_annotate_me = os.path.join(
            DATA_DIR,
            "01_annotate_me",
        )
        self.dir_02_corrected_textgrids = os.path.join(
            DATA_DIR,
            "02_corrected_textgrids",
        )
        self.dir_03_generated_transcripts = os.path.join(
            DATA_DIR,
            "03_generated_transcripts",
        )
        self.dir_04_submitted_transcripts = os.path.join(
            DATA_DIR,
            "04_submitted_transcripts",
        )
        self.dir_difficult_to_annotate = os.path.join(
            DATA_DIR,
            "difficult_to_annotate",
        )
        self.dir_tmp = os.path.join(DATA_DIR, "tmp")

        # Make sure paths exist.
        self._check_dirs_exist()

        # Load subject mapping.
        msg = "Loading subject mapping file from %s" % self.SUBJECT_MAPPING_PATH
        logger.info(msg)
        self.subject_mapping = {}
        for line in open(self.SUBJECT_MAPPING_PATH, "r"):
            line = line.strip()
            if line != "":
                mapping_i = line.split(",")
                if len(mapping_i) != 2:
                    raise Exception(
                        "Unable to parse line! More than 2 CSV values: %s" % line
                    )
                subject, map_value = mapping_i
                self.subject_mapping[subject] = map_value

        # Load my sections.
        msg = "Loading my_sections file from %s" % self.MY_SECTIONS_PATH
        logger.info(msg)
        self.my_sections = []
        for line in open(self.MY_SECTIONS_PATH, "r"):
            line = line.strip()
            if line != "":
                self.my_sections.append(line)

        # Create state.
        self.state = State(STATE_PATH)

        # ===================================================== #
        # THE STATE VARIABLES BELOW SHOULD BE RESET ON RESTART! #
        # ===================================================== #

        # Boolean flag for printing.
        self.printed_no_new_sections: bool = False

        # Boolean flag for whether we are currently requesting data. This way we
        # won't try to send two requests simultaneously.
        self.is_requesting_data: bool = False

        # Variable for storing the failed-download timeout information.
        self.next_download_time: datetime = None

    async def tick(self):
        # 1. Check if new data needs to be downloaded.
        await self._check_for_new_data()

        # 2. Check if there are any new corrected TextGrid files in
        #    02_corrected_textgrids/.
        #    If so,
        #     - move the corresponding WAV file from 01_annotate_me/ to
        #       02_corrected_textgrids/
        #     - delete the old TextGrid file from 01_annotate_me/
        #   (the same applies for difficult_to_annotate/)
        self._move_corrected_textgrids(
            source_dir=self.dir_01_annotate_me,  # user saves in difficult...
            dest_dir=self.dir_difficult_to_annotate,  # 01 -> difficult
        )
        self._move_corrected_textgrids(
            source_dir=self.dir_01_annotate_me,  # user saves in 02...
            dest_dir=self.dir_02_corrected_textgrids,  # check 01 -> 02
        )
        self._move_corrected_textgrids(
            source_dir=self.dir_difficult_to_annotate,  # ... but could also come from difficult
            dest_dir=self.dir_02_corrected_textgrids,  # check difficult -> 02
        )

        # 3. Check if there are any interview sections that are completely corrected.
        #    If so,
        #     - generate the transcript .txt file in 03_generated_transcripts/
        #     - delete the segment WAV/TextGrid files from 02_corrected_textgrids/
        self._generate_transcripts()

    def _check_dir_exists(self, dir_path, dir_name):
        dir_path = getattr(self, "dir_" + dir_name)
        if not os.path.exists(dir_path):
            msg = "The '%s' directory could not be found!" % dir_name
            msg += "\nExpected path: %s" % dir_path
            raise Exception(msg)

    def _check_dirs_exist(self):
        args_list = [
            (self.dir_01_annotate_me, "01_annotate_me"),
            (self.dir_02_corrected_textgrids, "02_corrected_textgrids"),
            (self.dir_03_generated_transcripts, "03_generated_transcripts"),
            (self.dir_04_submitted_transcripts, "04_submitted_transcripts"),
            (self.dir_difficult_to_annotate, "difficult_to_annotate"),
            (self.dir_tmp, "tmp"),
        ]
        for args in args_list:
            self._check_dir_exists(*args)

    async def _check_for_new_data(self):

        # Reference to asyncio loop, so we can schedule tasks for later (whenever
        # there is time).
        loop = asyncio.get_event_loop()

        # Extract section names for the "01_annotate_me" directory.
        sections_01 = self._extract_section_names(self.dir_01_annotate_me)

        # We will try to keep 2 sections in the queue. If we see that there is only
        # 1 section (or no sections) left, then we will request new data.
        if len(sections_01) < 2 and not self.is_requesting_data:
            self.is_requesting_data = True
            loop.create_task(self._start_requesting_data())

    async def _download_section(self, section_name: str):

        # Extract subject name.
        subject_name = section_name.split("_")[0]

        # URLs.
        CTM_URL = os.path.join(
            self.SERVER_URL_BASE,
            "data/fpack/ctm_init",
            self.subject_mapping[subject_name],
            subject_name,
            section_name + ".ctm",
        )
        WAV_URL = os.path.join(
            self.SERVER_URL_BASE,
            "data/fpack/audio/int16",
            self.subject_mapping[subject_name],
            subject_name,
            section_name + ".wav",
        )

        # Save paths.
        CTM_PATH = os.path.join(self.dir_tmp, section_name + ".ctm")
        WAV_PATH = os.path.join(self.dir_tmp, section_name + ".wav")

        # Fetch CTM file.
        msg = "Downloading CTM file for section '%s'..." % section_name
        logger.info(msg)
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(CTM_URL) as resp:
                    if resp.status == 200:
                        f = await aiofiles.open(CTM_PATH, mode="wb")
                        await f.write(await resp.read())
                        await f.close()
        except Exception as e:
            msg = "Failed to download CTM file from '%s' and save to '%s'."
            msg %= (CTM_URL, CTM_PATH)
            log_exception(logger, e)
            return False  # success == False

        # Fetch WAV file.
        msg = "Downloading WAV file for section '%s'..." % section_name
        logger.info(msg)
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(WAV_URL) as resp:
                    if resp.status == 200:
                        f = await aiofiles.open(WAV_PATH, mode="wb")
                        await f.write(await resp.read())
                        await f.close()
        except Exception as e:
            msg = "Failed to download WAV file from '%s' and save to '%s'."
            msg %= (WAV_URL, WAV_PATH)
            log_exception(logger, e)
            return False  # success == False

        # success == True
        return True

    def _extract_section_names(self, directory: str):
        section_names = []
        for file_name in sorted(os.listdir(directory)):
            base_name, ext = os.path.splitext(file_name)
            if ext != ".TextGrid":
                continue

            # Extract interview section name.
            # | e.g. s32_actual_BL_000.TextGrid --> s32_actual_BL
            section_name = base_name[:-4]
            if section_name not in section_names:
                section_names.append(section_name)
        return section_names

    async def _extract_section_segments(self, section_name: str):

        # Path to CTM file and full WAV file.
        ctm_path = os.path.join(self.dir_tmp, section_name + ".ctm")
        wav_path = os.path.join(self.dir_tmp, section_name + ".wav")

        # Make sure files exist.
        if not os.path.exists(ctm_path):
            msg = "Oops! Something went wrong. Unable to find CTM file: %s"
            msg %= ctm_path
            logger.error(msg)
            return False  # success == False
        if not os.path.exists(wav_path):
            msg = "Oops! Something went wrong. Unable to find WAV file: %s"
            msg %= wav_path
            logger.error(msg)
            return False  # success == False

        # Extract segments from CTM file and full WAV file.
        msg = "Extracting segment TextGrid/WAV file for '%s'." % section_name
        logger.info(msg)
        try:
            converter = CtmConverter(
                use_ref=False,
                base_name=section_name,
                ctm_path=ctm_path,
                audio_path=wav_path,
            )
            output_dir = self.dir_01_annotate_me
            await converter.write_textgrids_async(
                textgrids_dir=output_dir,
                audio_segments_dir=output_dir,
            )
        except Exception as e:
            msg = "Failed to extract TextGrid/audio segments from the files '%s' and '%s'."
            msg %= (ctm_path, wav_path)
            log_exception(logger, e)
            return False  # success == False

        # Remove files from tmp/ dir.
        self._remove_file(ctm_path)
        self._remove_file(wav_path)

        # success == True
        return True

    def _remove_file(self, path: str):
        try:
            os.remove(path)
        except:
            pass

    def _generate_transcripts(self):

        # Extract section names for the first two directories.
        sections_01 = self._extract_section_names(self.dir_01_annotate_me)
        sections_02 = self._extract_section_names(self.dir_02_corrected_textgrids)
        sections_difficult = self._extract_section_names(self.dir_difficult_to_annotate)

        # Difficult sections are still in first stage of pipeline.
        sections_01.extend(sections_difficult)

        # Check if there are sections in the "02_corrected_textgrids" directory that
        # no longer exist in the "01_annotate_me" directory, i.e. the section is
        # completely annotated.
        for section in sections_02:

            if section not in sections_01:
                msg = "Detected finished interview section '%s'!" % section
                logger.info(msg)

                # Construct utterance from TextGrid files.
                glob_name = "%s_*.TextGrid" % section
                glob_path = os.path.join(self.dir_02_corrected_textgrids, glob_name)
                textgrid_paths = sorted(glob.glob(glob_path))
                if len(textgrid_paths) == 0:
                    msg = "Oops! Something went wrong. The corresponding TextGrid "
                    msg += "files could not be found using the glob path "
                    msg += "'%s'." % glob_path
                    logger.error(msg)
                    continue
                msg = "Generating transcript from %i TextGrid files."
                msg %= len(textgrid_paths)
                logger.info(msg)
                utt = textgrid_to_utterance(textgrid_paths)

                # Save result in 03_generated_transcripts.
                transcript_name = "%s.txt" % section
                transcript_path = os.path.join(
                    self.dir_03_generated_transcripts, transcript_name
                )
                msg = "Saving transcript to %s" % transcript_path
                logger.info(msg)
                if os.path.exists(transcript_path):
                    msg = "Transcript already exists! Overwriting..."
                    logger.warning(msg)
                with open(transcript_path, "w") as f:
                    f.write(utt)

                # Remove TextGrid and WAV files from 02_corrected_textgrids. The
                # files from 01_annotate_me have already been removed by
                # `_move_corrected_textgrids()`.
                glob_name_textgrid = "%s_*.TextGrid" % section
                glob_name_wav = "%s_*.wav" % section
                glob_path_textgrid = os.path.join(
                    self.dir_02_corrected_textgrids, glob_name_textgrid
                )
                glob_path_wav = os.path.join(
                    self.dir_02_corrected_textgrids, glob_name_wav
                )
                textgrid_paths = sorted(glob.glob(glob_path_textgrid))
                wav_paths = sorted(glob.glob(glob_path_wav))

                # --> Remove TextGrid files.
                msg = "Removing %i TextGrid files..." % len(textgrid_paths)
                logger.info(msg)
                for path in textgrid_paths:
                    msg = "> Removing %s" % path
                    self._remove_file(path)

                # --> Remove WAV files.
                msg = "Removing %i WAV files..." % len(wav_paths)
                logger.info(msg)
                for path in wav_paths:
                    msg = "> Removing %s" % path
                    self._remove_file(path)

    def _move_corrected_textgrids(self, source_dir: str, dest_dir: str):

        # Extract name of source_dir and dest_dir for logging.
        source_dir_str = os.path.basename(source_dir) + "/"
        dest_dir_str = os.path.basename(dest_dir) + "/"

        for file_name in os.listdir(dest_dir):

            base_name, ext = os.path.splitext(file_name)
            if ext != ".TextGrid":
                continue

            # ===================== #
            # Process TextGrid File #
            # ===================== #

            # 1. Check if we've already moved the .wav file and deleted the old
            #    TextGrid.
            wav_name = "%s.wav" % base_name
            old_wav_path = os.path.join(source_dir, wav_name)
            new_wav_path = os.path.join(dest_dir, wav_name)
            has_moved_wav = os.path.exists(new_wav_path)

            old_tg_path = os.path.join(source_dir, file_name)
            has_removed_tg = not os.path.exists(old_tg_path)

            if not has_moved_wav and not has_removed_tg:
                msg = "Detected new corrected TextGrid: %s." % file_name
                logger.info(msg)

            # 2. Move/delete the files if necessary.
            if not has_moved_wav:
                if os.path.exists(old_wav_path):
                    msg = "> Moving WAV file to %s folder."
                    msg %= dest_dir_str
                    logger.info(msg)
                    try:
                        os.rename(old_wav_path, new_wav_path)
                    except Exception as e:
                        msg = "Failed to move WAV file from %s to %s"
                        msg %= (old_wav_path, new_wav_path)
                        logger.error(msg)
                        log_exception(logger, e)

            if not has_removed_tg:
                msg = "> Removing old TextGrid file from %s folder."
                msg %= source_dir_str
                logger.info(msg)
                try:
                    os.remove(old_tg_path)
                except Exception as e:
                    msg = "Failed to remove TextGrid file %s" % old_tg_path
                    logger.error(msg)
                    log_exception(logger, e)

            if has_moved_wav and os.path.exists(old_wav_path):
                # No need to store the wav file twice...
                msg = "Removing duplicate WAV file: %s" % old_wav_path
                msg += "\nNote: this file already exists here '%s'." % new_wav_path
                logger.info(msg)
                try:
                    os.remove(old_wav_path)
                except Exception as e:
                    msg = "Failed to remove WAV file %s" % old_wav_path
                    logger.error(msg)
                    log_exception(logger, e)

    async def _start_requesting_data(self):

        # Are we waiting for failed download timeout?
        if self.next_download_time is not None:
            if datetime.now() <= self.next_download_time:
                # Reset flag, so we will try again shortly.
                self.is_requesting_data = False
                return

        # Check if there are still sections to request.
        next_section = None
        for section_name in self.my_sections:
            if not self.state.has_extracted_section(section_name):
                next_section = section_name
                break

        # Start logger message...
        msg = "Detected less than 2 interview sections in '01_annotate_me'."
        msg += "\nChecking if there are still sections to fetch..."

        if next_section is None:
            if not self.printed_no_new_sections:
                # ... finish logger message.
                msg += "\nThere are no new interview sections to request."
                msg += "\nIf you would like to change your sections, please modify "
                msg += "the file 'collaboration/my_sections.txt'."
                logger.info(msg)
                self.printed_no_new_sections = True
            # Reset flag, so we will try again shortly.
            self.is_requesting_data = False
            return

        # Reset flag.
        self.printed_no_new_sections = False

        # ... finish logger message.
        msg += "\nNew data found for interview section: %s." % next_section
        logger.info(msg)

        # Download new CTM/WAV data.
        if not self.state.has_downloaded_section(next_section):
            success = await self._download_section(next_section)
            if success:
                # Update state so the program remembers its progress when the app is closed.
                self.state.finished_downloading_section(next_section)
            else:
                # Update failed timeout variable.
                self.next_download_time = datetime.now() + timedelta(
                    seconds=self.DOWNLOAD_FAIL_TIMEOUT_SECS
                )
                # Reset flag, so we will try again shortly.
                self.is_requesting_data = False
                return

        # Extract TextGrid/audio segments.
        success = await self._extract_section_segments(next_section)
        if success:
            # Update state so the program remembers its progress when the app is closed.
            self.state.finished_extracting_section(next_section)
        else:
            # Update failed timeout variable.
            self.next_download_time = datetime.now() + timedelta(
                seconds=self.DOWNLOAD_FAIL_TIMEOUT_SECS
            )
            # Reset flag, so we will try again shortly.
            self.is_requesting_data = False
            return

        # Finished!
        msg = "Successfully downloaded and extracted segments for section '%s'."
        msg %= next_section
        logger.info(msg)

        # Reset flag, so we are able to request more data later.
        self.is_requesting_data = False
