#!/bin/bash

# Change working directory to this script's directory.
# Source: https://stackoverflow.com/a/10348989
# Example: https://stackoverflow.com/a/55798664
#
# Directory containing Bash script, i.e. "install/common/create_venv/".
script_dir="$(dirname $(realpath "${BASH_SOURCE[0]}"))"
root_dir="${script_dir}/../../.."
# Relative path to script directory.
script_dir_rel="install/common/create_venv"
# Original working directory.
original_working_dir=$PWD

# Move to root directory.
cd $root_dir


if [[ "$OSTYPE" == "msys" ]]; then
    # Windows.
    echo "Creating create_venv.sh (Windows)..."
    ln -s "${script_dir_rel}/create_venv.windows.sh" create_venv.sh
    echo "Done."
else
    # Linux.
    echo "Creating create_venv.sh (Linux)..."
    ln -s "${script_dir_rel}/create_venv.linux.sh" create_venv.sh
    echo "Done."
fi

# Restore original working directory.
cd $original_working_dir