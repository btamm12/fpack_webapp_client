import asyncio
import os
from praatio import audio, textgrid
from typing import List
from scipy.io import wavfile

from .ctm_line import CtmLine
from logger import logger


class CtmConverter:
    def __init__(
        self,
        use_ref: bool,
        base_name: str,
        ctm_path: str,
        audio_path: str,
        SEGMENT_DURATION_SEC: float = 15,
        MIN_SEGMENT_LENGTH_FACTOR: float = 0.5,
        MIN_SILENCE_SEC: float = 0.150,
        MIN_WORD_SEC: float = 0,
    ) -> None:

        # Check inputs.
        assert os.path.exists(ctm_path), "ctm_path '%s' does not exist." % ctm_path
        assert os.path.exists(audio_path), (
            "audio_path '%s' does not exist." % audio_path
        )
        assert (
            SEGMENT_DURATION_SEC > 0
        ), "SEGMENT_DURATION_SEC must be a positive float."
        assert (
            MIN_SEGMENT_LENGTH_FACTOR > 0 and MIN_SEGMENT_LENGTH_FACTOR <= 1
        ), "MIN_SEGMENT_LENGTH_FACTOR must be a float in (0,1]."
        assert MIN_SILENCE_SEC >= 0, "MIN_SILENCE_SEC must be a float in [0,+inf)"
        assert MIN_WORD_SEC >= 0, "MIN_WORD_SEC must be a float in [0,+inf)"

        # Save inputs for debugging.
        self.base_name = base_name
        self.ctm_path = ctm_path
        self.audio_path = audio_path
        self.SEGMENT_DURATION_SEC = SEGMENT_DURATION_SEC
        self.MIN_SEGMENT_LENGTH_FACTOR = MIN_SEGMENT_LENGTH_FACTOR
        self.MIN_SILENCE_SEC = MIN_SILENCE_SEC
        self.MIN_WORD_SEC = MIN_WORD_SEC

        # Parse lines.
        with open(ctm_path, encoding="utf-8", mode="r") as f:
            ctm_lines = [CtmLine(use_ref, line=line) for line in f]

        # Append silences.
        eps = 1e-5
        i = 0
        while i < len(ctm_lines) - 1:
            # Insert silence?
            if ctm_lines[i + 1].start > ctm_lines[i].end + eps:
                ctm_lines.insert(
                    i + 1,
                    CtmLine(
                        use_ref,
                        utt_id=ctm_lines[i].utt_id,
                        channel=ctm_lines[i].channel,
                        start=ctm_lines[i].end,
                        end=ctm_lines[i + 1].start,
                        word="",
                        score=1.0,
                    ),
                )
                continue

            # Remove overlap?
            if ctm_lines[i + 1].start < ctm_lines[i].end - eps:
                if ctm_lines[i + 1].score <= ctm_lines[i].score:
                    # Move next line's start bound.
                    ctm_lines[i + 1].start = ctm_lines[i].end
                else:
                    # Move this line's end bound.
                    ctm_lines[i].end = ctm_lines[i + 1].start

            # Remove segments that are too short.
            if ctm_lines[i].word == "":
                min_len = self.MIN_SILENCE_SEC
            else:
                min_len = self.MIN_WORD_SEC
            if ctm_lines[i].end - ctm_lines[i].start < min_len + eps:
                # Short silences are divied over neighboring words.
                if ctm_lines[i].word == "":
                    duration = ctm_lines[i].end - ctm_lines[i].start
                    if i > 0:
                        ctm_lines[i - 1].end += duration / 2
                        ctm_lines[i + 1].start -= duration / 2
                    else:
                        ctm_lines[i + 1].start -= duration
                ctm_lines.remove(ctm_lines[i])
                continue

            i += 1

        self.data = {
            "audio_path": audio_path,
            "ctm_lines": ctm_lines,
            "utterance": self._lines_to_utterance(ctm_lines),
        }

    def _interval_to_str(self, start: float, end: float, value: str):
        return "(start=%0.4f,end=%0.4f,value=%s)" % (start, end, value)

    def _fix_rounding_errors(self, entries, minT, maxT):
        new_entries = []
        last_start = None
        last_end = None
        last_value = None
        for start, end, value in entries:

            # Make copies, so we can still log the original variables.
            new_start = start
            new_end = end

            # Check valid start/end times. Print error message if error is too large.
            eps = 1e-3
            if new_start < minT:
                if minT - new_start > eps:
                    msg = "Problem with interval %s: start time is smaller than minT (%0.4f)."
                    msg %= (self._interval_to_str(start, end, value), minT)
                    logger.error(msg)
                new_start = minT
            if new_end > maxT:
                if new_end - maxT > eps:
                    msg = "Problem with interval %s: end time is larger than maxT (%0.4f)."
                    msg %= (self._interval_to_str(start, end, value), maxT)
                    logger.error(msg)
                new_end = maxT

            # Also check if this start time is not before the previous end time.
            if last_end is not None and new_start < last_end:
                if last_end - new_start > eps:
                    msg = "Problem with consecutive intervals %s, %s: start time is smaller than previous end time."
                    msg %= (
                        self._interval_to_str(last_start, last_end, last_value),
                        self._interval_to_str(start, end, value),
                    )
                    logger.error(msg)
                new_start = last_end

            # Make sure the interval is not zero-length!
            if new_start > new_end - eps:
                msg = "Problem with interval %s: interval duration collapses to 0 seconds."
                msg += "Calculation used 'corrected interval' %s."
                msg += "Removing interval..."
                msg %= (
                    self._interval_to_str(start, end, value),
                    self._interval_to_str(new_start, new_end, value),
                )
                logger.error(msg)
                continue

            # Add the interval to the new entry list.
            new_entries.append((new_start, new_end, value))

            # Remember last interval.
            last_start, last_end, last_value = start, end, value

        return new_entries

    def _calculate_segment_end(
        self,
        segment_start: float,
        audio_duration: float,
    ):
        nominal_end = segment_start + self.SEGMENT_DURATION_SEC
        nearest_end = self._get_nearest_bound(nominal_end, "end")
        offset = nearest_end - nominal_end
        max_offset = self.SEGMENT_DURATION_SEC * self.MIN_SEGMENT_LENGTH_FACTOR
        if offset > max_offset:
            segment_end = nominal_end
        else:
            segment_end = nearest_end

        # Make sure final segment is long enough.
        rest = audio_duration - segment_end
        if rest < max_offset:
            segment_end = audio_duration

        return segment_end

    def _get_nearest_bound(self, time: float, bound: str):
        # bound must be either "start" or "end"
        if bound not in {"start", "end"}:
            raise Exception("bound must be 'start' or 'end'.")

        ctm_lines: List[CtmLine] = self.data["ctm_lines"]
        min_dist = None
        best_line = None
        for line in ctm_lines:

            # Calculate error. Positive error means the line is after the desired
            # time.
            if bound == "start":
                err = line.start - time
            if bound == "end":
                err = line.end - time

            cur_dist = abs(err)
            # Assuming lines are chronologically ordered, define exit clause.
            if min_dist is not None and err > 0 and cur_dist > min_dist:
                break
            # Save minimum distance?
            if min_dist is None or cur_dist < min_dist:
                min_dist = cur_dist
                best_line = line

        # Return best value.
        if best_line is None:
            return None
        elif bound == "start":
            return best_line.start
        elif bound == "end":
            return best_line.end

    def _filter_lines(
        self, lines: List[CtmLine], start_time: float = None, end_time: float = None
    ):
        eps = 1e-3
        filtered = False
        # Filter words occurring after `start_time`.
        if start_time is not None:
            lines = filter(lambda x: x.start > start_time - eps, lines)
            filtered = True
        # Filter words occurring before `end_time`.
        if end_time is not None:
            lines = filter(lambda x: x.end < end_time + eps, lines)
            filtered = True

        if filtered:
            return list(lines)
        else:
            return lines

    def _lines_to_utterance(
        self, lines: List[CtmLine], start_time: float = None, end_time: float = None
    ):
        # Works best if start_time/end_time are at a word boundary!

        # Filter lines based on desired start/end times.
        lines = self._filter_lines(lines, start_time, end_time)

        # Filter out silences.
        lines = filter(lambda x: x.word != "", lines)

        # Return utterance.
        return " ".join(x.word for x in lines)

    async def write_textgrids_async(
        self,
        textgrids_dir: str,
        audio_segments_dir: str,
        context_secs: float = 0,
        sleep_secs: float = 0.1,
    ):
        # Create output directories.
        if not os.path.exists(textgrids_dir):
            os.makedirs(textgrids_dir)
        if not os.path.exists(audio_segments_dir):
            os.makedirs(audio_segments_dir)

        audio_path: str = self.data["audio_path"]
        ctm_lines: List[CtmLine] = self.data["ctm_lines"]

        # Calculate audio duration and number of segments.
        audio_duration = audio.getDuration(audio_path)

        # Load audio file.
        fs, audio_data = wavfile.read(audio_path)

        # Process per segment.
        segment_idx = 0
        segment_start = 0
        segment_end = self._calculate_segment_end(
            segment_start,
            audio_duration,
        )
        eps = 1e-3
        while segment_start + eps < audio_duration:

            # Give other threads a chance to run.
            await asyncio.sleep(sleep_secs)

            # Calculate start/end context duration. This will add X seconds to
            # start/end of audio in order to provide a bit of context. Of course,
            # this is not possible at the start/end of the file.
            start_context = min(segment_start, context_secs)
            end_context = min(audio_duration - segment_end, context_secs)

            # Calculate lines.
            filtered_lines = self._filter_lines(
                ctm_lines,
                start_time=segment_start,
                end_time=segment_end,
            )

            # Calculate utterance.
            segment_utterance = self._lines_to_utterance(filtered_lines)

            # ==================== #
            # CREATE AUDIO SEGMENT #
            # ==================== #

            # Make sure we include the context audio!
            audio_start = max(int((segment_start - start_context) * fs), 0)
            audio_end = min(int((segment_end + end_context) * fs), len(audio_data))
            audio_segment_data = audio_data[audio_start:audio_end]
            audio_segment_path = os.path.join(
                audio_segments_dir,
                "%s_%03i.wav" % (self.base_name, segment_idx),
            )
            wavfile.write(audio_segment_path, fs, audio_segment_data)

            # =============== #
            # CREATE TEXTGRID #
            # =============== #
            tg = textgrid.Textgrid()

            minT = 0
            maxT = segment_end - segment_start + start_context + end_context

            # Construct entries for each tier.
            utt_entries = [
                (minT + start_context, maxT - end_context, segment_utterance)
            ]
            word_entries = [
                x.word_entry(offset=-segment_start + start_context)
                for x in filtered_lines
            ]
            score_entries = [
                x.score_entry(offset=-segment_start + start_context)
                for x in filtered_lines
            ]

            # Add an entry for each context area in the 3 tiers.
            if start_context > 0:
                entry_times = (minT, start_context)
                # Utt tier.
                entry = (*entry_times, "Start context: do not annotate this part!")
                utt_entries.insert(0, entry)
                # Word tier.
                entry = (*entry_times, "/CONTEXT/")
                word_entries.insert(0, entry)
                # Score tier.
                entry = (*entry_times, "/")
                score_entries.insert(0, entry)
            if end_context > 0:
                entry_times = (maxT - end_context, maxT)
                # Utt tier.
                entry = (*entry_times, "End context: do not annotate this part!")
                utt_entries.append(entry)
                # Word tier.
                entry = (*entry_times, "/CONTEXT/")
                word_entries.append(entry)
                # Score tier.
                entry = (*entry_times, "/")
                score_entries.append(entry)

            # Fix any rounding errors.
            utt_entries = self._fix_rounding_errors(utt_entries, minT, maxT)
            word_entries = self._fix_rounding_errors(word_entries, minT, maxT)
            score_entries = self._fix_rounding_errors(score_entries, minT, maxT)

            # Create the Tiers.
            utt_tier = textgrid.IntervalTier(
                name="utterance",
                entryList=utt_entries,
                minT=minT,
                maxT=maxT,
            )
            word_tier = textgrid.IntervalTier(
                name="words",
                entryList=word_entries,
                minT=minT,
                maxT=maxT,
            )
            score_tier = textgrid.IntervalTier(
                name="scores",
                entryList=score_entries,
                minT=minT,
                maxT=maxT,
            )

            # Add the tiers.
            tg.addTier(utt_tier)
            tg.addTier(word_tier)
            tg.addTier(score_tier)

            # Write the file.
            textgrid_segment_path = os.path.join(
                textgrids_dir,
                "%s_%03i.TextGrid" % (self.base_name, segment_idx),
            )
            tg.save(
                textgrid_segment_path,
                format="short_textgrid",
                includeBlankSpaces=False,
            )

            # Next segment.
            segment_idx += 1
            segment_start = segment_end
            segment_end = self._calculate_segment_end(
                segment_start,
                audio_duration,
            )
