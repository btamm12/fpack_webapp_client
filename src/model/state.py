import os
import pickle
from typing import Dict, List, Union


class State:

    _state: Dict = None
    _startup_needs_extraction: bool = False

    @property
    def _downloaded_reviews(self) -> List[str]:
        return self._state["downloaded_reviews"]

    @property
    def _downloaded_sections(self) -> List[str]:
        return self._state["downloaded_sections"]

    @property
    def _extracted_sections(self) -> List[str]:
        return self._state["extracted_sections"]

    def __init__(self, SAVE_PATH: str):
        _, ext = os.path.splitext(SAVE_PATH)
        if ext != ".pkl":
            msg = "SAVE_PATH must have the extension '.pkl'. Current save path: %s"
            msg %= SAVE_PATH
            raise Exception(msg)

        # Save path.
        self.SAVE_PATH = SAVE_PATH

        # Make sure directory exists.
        save_dir = os.path.dirname(SAVE_PATH)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # Load state if it exists. Otherwise create new blank state.
        if os.path.exists(self.SAVE_PATH):
            self._load_state()
        else:
            self._state = {
                "downloaded_reviews": [],
                "downloaded_sections": [],
                "extracted_sections": [],
            }
            self.state_changed()

        # Extraction needed at startup?
        downloaded_set = set(self._downloaded_sections)
        extracted_set = set(self._extracted_sections)
        diff_set = downloaded_set.difference(extracted_set)
        self._startup_needs_extraction = len(diff_set) > 0

    def finished_downloading_review(self, review_name: str):
        self._downloaded_reviews.append(review_name)
        self.state_changed()

    def finished_downloading_section(self, section_name: str):
        self._downloaded_sections.append(section_name)
        self.state_changed()

    def finished_extracting_section(self, section_name: str):
        self._startup_needs_extraction = False
        self._extracted_sections.append(section_name)
        self.state_changed()

    def has_downloaded_review(self, review_name: str):
        return review_name in self._downloaded_reviews

    def has_downloaded_section(self, section_name: str):
        return section_name in self._downloaded_sections

    def has_extracted_section(self, section_name: str):
        return section_name in self._extracted_sections

    def state_changed(self):
        self._save_state()

    def _save_state(self):
        with open(self.SAVE_PATH, "wb") as f:
            pickle.dump(self._state, f)

    def _load_state(self):
        with open(self.SAVE_PATH, "rb") as f:
            self._state = pickle.load(f)
        # Backwards compatability:
        # - Added in v0.2.0
        if "downloaded_reviews" not in self._state:
            self._state["downloaded_reviews"] = []
        # - Added in v0.1.0
        if "downloaded_sections" not in self._state:
            self._state["downloaded_sections"] = []
        if "extracted_sections" not in self._state:
            self._state["extracted_sections"] = []
