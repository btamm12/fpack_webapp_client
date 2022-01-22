import os
from utils import CtmConverter

# Path to predicted CTM directory.
ctm_dir = "../../users/btamm/output/predict"
assert os.path.exists(ctm_dir)

# Path to directory containing audio files.
audio_dir = "../../data/fpack/audio/int16/s32"
assert os.path.exists(audio_dir)

# Output directory.
output_textgrids_dir = "./textgrids"
output_audio_dir = "./audio_segments"

for ctm_file in sorted(os.listdir(ctm_dir)):
    print("Processing '%s'..." % ctm_file)
    ctm_path = os.path.join(ctm_dir, ctm_file)
    if not os.path.isfile(ctm_path):
        continue
    base_name, ext = os.path.splitext(ctm_file)
    if ext != ".ctm":
        continue
    audio_path = os.path.join(audio_dir, "%s.wav" % base_name)

    # Load CTM file, parse and write to TextGrid files.
    converter = CtmConverter(
        use_ref=False,
        base_name=base_name,
        ctm_path=ctm_path,
        audio_path=audio_path,
    )
    converter.write_textgrids(output_textgrids_dir, output_audio_dir)


