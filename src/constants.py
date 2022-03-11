from pathlib import Path


# ===== #
# PATHS #
# ===== #

# 1. MAIN FOLDERS

# fpack_webapp_client/
DIR_PROJECT = Path(__file__).resolve().parents[1]

# fpack_webapp_client/collaboration/
DIR_COLLABORATION = DIR_PROJECT.joinpath("collaboration")

# fpack_webapp_client/data/
DIR_DATA = DIR_PROJECT.joinpath("data")

# fpack_webapp_client/src/
DIR_SRC = DIR_PROJECT.joinpath("src")

# 2. SPECIFIC FILES

# Subject mapping file.
SUBJECT_MAPPING_PATH = DIR_PROJECT.joinpath("subject_mapping.txt")
# Version file.
VERSION_PATH = DIR_PROJECT.joinpath("version.txt")
# my_name file.
MY_NAME_PATH = DIR_COLLABORATION.joinpath("my_name.txt")
# my_sections file.
MY_SECTIONS_PATH = DIR_COLLABORATION.joinpath("my_sections.txt")
# state.pkl file.
STATE_PATH = DIR_SRC.joinpath("state.pkl")
