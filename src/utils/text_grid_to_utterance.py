import glob
import os
from praatio import textgrid
from praatio.data_classes.interval_tier import Interval, IntervalTier


def text_grid_to_utterance(text_grid_glob: str):
    text_grid_paths = sorted(glob.glob(text_grid_glob))
    if len(text_grid_paths) == 0:
        raise Exception("Glob returned no paths for %s." % text_grid_glob)

    words = []

    for text_grid_path in text_grid_paths:

        # Load TextGrid.
        tg = textgrid.openTextgrid(text_grid_path, includeEmptyIntervals=False)

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
