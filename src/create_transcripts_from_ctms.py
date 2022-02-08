from utils import CtmLine

import os
from typing import List


class _CtmConverter:
    def __init__(
        self,
        use_ref: bool,
        base_name: str,
        ctm_path: str,
        SEGMENT_DURATION_SEC: float = 15,
        MIN_SEGMENT_LENGTH_FACTOR: float = 0.5,
        MIN_SILENCE_SEC: float = 0.150,
        MIN_WORD_SEC: float = 0,
    ) -> None:

        # Check inputs.
        assert os.path.exists(ctm_path), "ctm_path '%s' does not exist." % ctm_path
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

        # Heuristic punctuation based on silences.
        silences = []
        for line in ctm_lines:
            if line.word == "":
                silences.append(line.end - line.start)

        # Punctuation threshold = longest xx% of silences
        PUNC_THRESHOLD = 0.40
        silences_sort = sorted(silences)
        idx = int(PUNC_THRESHOLD * len(silences_sort))
        PUNC_SILENCE_DURATION = silences_sort[idx]

        # Likely sentence starts for punctuation.
        likely_starts = [
            *("ik", "jij", "je", "hij", "zij", "ze", "u", "jullie"),
            *("de", "het", "dit", "dat"),
            *("en", "maar", "dus", "dan", "toen"),
        ]

        # Insert punctuation.
        last_punctuation = -1
        i = 0
        while i < len(ctm_lines):

            # Don't allow short sentences (minimum 3 words)
            # ".  A  B  ."
            #  0* 1  2  3*
            if i - last_punctuation <= 3:
                i += 1
                continue

            line = ctm_lines[i]
            line_duration = line.end - line.start
            if line.word == "" and line_duration > PUNC_SILENCE_DURATION:

                # Search for likely sentence starts.
                j = i + 1
                while j < len(ctm_lines):
                    line_j = ctm_lines[j]
                    if not line_j.is_filler and line_j.word != "":
                        if line_j.word in likely_starts:
                            line.word = "."
                            i = j
                            last_punctuation = j
                        break
                    j += 1

                # Final word ends with period.
                if i == len(ctm_lines) - 1:
                    line.word = "."

            i += 1

        self.data = {
            "ctm_lines": ctm_lines,
            "utterance": self.lines_to_utterance(ctm_lines),
        }

    def lines_to_utterance(self, lines: List[CtmLine]):
        # Works best if start_time/end_time are at a word boundary!

        # Filter out silences.
        lines = filter(lambda x: x.word != "", lines)

        # Return utterance.
        return " ".join(x.word for x in lines)


if __name__ == "__main__":

    root_dir = "/mnt/data/Ubuntu/ctms/ctm_init"
    out_dir = "/mnt/data/Ubuntu/ctms/transcripts_punc_v5"

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    for pseudo_name in os.listdir(root_dir):
        pseudo_dir = os.path.join(root_dir, pseudo_name)
        subject_name = os.listdir(pseudo_dir)[0]
        subject_dir = os.path.join(pseudo_dir, subject_name)

        for ctm_file in os.listdir(subject_dir):
            ctm_path = os.path.join(subject_dir, ctm_file)
            base_name = os.path.splitext(ctm_file)[0]

            converter = _CtmConverter(
                use_ref=False,
                base_name=base_name,
                ctm_path=ctm_path,
            )
            utt = converter.data["utterance"]

            # Output file
            output_dir = os.path.join(out_dir, subject_name)
            output_path = os.path.join(output_dir, base_name + ".txt")
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            with open(output_path, encoding="utf-8", mode="w") as f:
                f.write(utt + "\n")
