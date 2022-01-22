class CtmLine:
    def __init__(
        self,
        use_ref: bool,
        utt_id: str = None,
        channel: int = None,
        start: float = None,
        duration: float = None,
        end: float = None,
        word: str = None,
        score: float = None,
        line: str = None,
    ) -> None:

        # BUG IN CODE: timing is off
        if use_ref:
            FACTOR = 1
        else:
            FACTOR = 3

        # Parse line.
        if line is not None:
            parts = line.strip().split(" ")
            if use_ref:
                assert len(parts) == 5
            else:
                assert len(parts) == 6
            self.utt_id = parts[0]
            self.channel = int(parts[1])
            self.start = float(parts[2]) * FACTOR
            self.duration = float(parts[3]) * FACTOR
            self.word = self._remove_filler(parts[4])
            if use_ref:
                self.score = 1
            else:
                self.score = float(parts[5])
        else:
            assert utt_id is not None
            assert channel is not None
            assert start is not None
            assert duration is not None or end is not None
            assert word is not None
            assert score is not None

            self.utt_id = utt_id
            self.channel = channel
            self.start = start
            if end is not None:
                self.end = end
                self.duration = end - start
            elif duration is not None:
                self.duration = duration
                self.end = self.start + self.duration
            self.word = self._remove_filler(word)
            self.score = score

        # Calculate end time.
        self.end = self.start + self.duration


    def _remove_filler(self, word: str):
        try:
            idx = word.index(",filler")
            return word[:idx]
        except:
            return word

    def word_entry(self, offset: float = None):
        if offset is None:
            return (
                round(self.start, 5),
                round(self.end, 5),
                self.word,
            )
        else:
            return (
                round(self.start + offset, 5),
                round(self.end + offset, 5),
                self.word,
            )

    def score_entry(self, offset: float = None):
        if offset is None:
            return (
                round(self.start, 5),
                round(self.end, 5),
                "%0.2f" % self.score,
            )
        else:
            return (
                round(self.start + offset, 5),
                round(self.end + offset, 5),
                "%0.2f" % self.score,
            )
