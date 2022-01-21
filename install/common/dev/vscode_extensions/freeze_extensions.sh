#!/bin/bash

# Change working directory to this script's directory.
# Source: https://stackoverflow.com/a/10348989
# Example: https://stackoverflow.com/a/55798664
#
# Directory containing Bash script, i.e. "install/common/dev/vscode_launch/".
script_dir="$(dirname $(realpath "${BASH_SOURCE[0]}"))"
# Original working directory.
original_working_dir=$PWD

# Move to script directory.
cd $script_dir

# Write extensions to "extensions.txt"
code --list-extensions | cat > extensions.txt

# Restore original working directory.
cd $original_working_dir