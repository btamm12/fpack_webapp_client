import os
from utils import text_grid_to_utterance

# File to process.
base_name = "s32_bio_part1_BL"

# Glob path to TextGrid files.
textgrid_glob = "./textgrids/%s_*.TextgGrid" % base_name

# Output path for utterance.
utterance_dir = "./utterances"
utterance_path = os.path.join(utterance_dir, "%s.txt" % base_name)

print("Extracting utterance from TextGrid files...")
utt = text_grid_to_utterance(textgrid_glob)


# Create output directory.
if not os.path.exists(utterance_dir):
    os.makedirs(utterance_dir)

# Write to output file.
print("Writing to output file...")
with open(utterance_path, "w") as f:
    f.write(utt)

print("Finished.")
