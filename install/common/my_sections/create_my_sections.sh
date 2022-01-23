#!/bin/bash

# Directory calculations:
# Source: https://stackoverflow.com/a/10348989
# Example: https://stackoverflow.com/a/55798664

# Directory containing Bash script, i.e. "install/common/create_venv/".
script_dir="$(dirname $(realpath "${BASH_SOURCE[0]}"))"
collab_dir="${script_dir}/../../../collaboration"
# Original working directory.
original_working_dir=$PWD

# Move to root directory.
cd $collab_dir

# Create file.
touch "my_sections.txt"

# Restore original working directory.
cd $original_working_dir