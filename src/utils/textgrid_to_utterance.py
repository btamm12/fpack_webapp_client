import glob
import os
from praatio import textgrid
from praatio.data_classes.interval_tier import Interval, IntervalTier
from typing import List


def textgrid_to_utterance(textgrid_paths: List[str]):

    words = []

    for textgrid_path in textgrid_paths:

        # Load TextGrid.
        tg = textgrid.openTextgrid(textgrid_path, includeEmptyIntervals=False)

        # Go through "words" Tier.
        if "words" not in tg.tierNameList:
            raise Exception("'words' not found in tier list of TextGrid.")
        words_tier: IntervalTier = tg.tierDict["words"]
        if words_tier.entryType != Interval:
            raise Exception("'words' tier is not an interval tier.")
        for entry in words_tier.entryList:
            value: str = entry[2]
            words.extend(value.strip().split())

    return " ".join(words)
