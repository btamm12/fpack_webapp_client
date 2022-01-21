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

# Install extensions.
cat extensions.txt | while read extension || [[ -n $extension ]];
do
  code --install-extension $extension
done

clear
echo "-------------------------------------------"
echo "| Restart VSCode for this to take effect! |"
echo "-------------------------------------------"

# Restore original working directory.
cd $original_working_dir