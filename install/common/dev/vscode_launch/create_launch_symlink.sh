#!/bin/bash

# Change working directory to this script's directory.
# Source: https://stackoverflow.com/a/10348989
# Example: https://stackoverflow.com/a/55798664
#
# Directory containing Bash script, i.e. "install/common/dev/vscode_launch/".
script_dir="$(dirname $(realpath "${BASH_SOURCE[0]}"))"
vscode_dir="${script_dir}/../../../../.vscode"
# Relative path to script directory.
script_dir_rel="../install/common/dev/vscode_launch"
# Original working directory.
original_working_dir=$PWD

# Move to vscode directory.
cd $vscode_dir


if [[ "$OSTYPE" == "msys" ]]; then
    # Windows.
    echo "Creating launch.json (Windows)..."
    ln -s "${script_dir_rel}/launch.windows.json" launch.json
    echo "Done."
else
    # Linux.
    echo "Creating launch.json (Linux)..."
    ln -s "${script_dir_rel}/launch.linux.json" launch.json
    echo "Done."
fi

# Restore original working directory.
cd $original_working_dir