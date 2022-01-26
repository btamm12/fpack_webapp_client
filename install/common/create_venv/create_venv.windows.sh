#!/bin/bash

# Directory where virtual environment will be installed, i.e. root directory.
install_dir="$(realpath $(dirname "${BASH_SOURCE[0]}"))"
# Original working directory.
original_working_dir=$PWD

# ========================================================== #
# Install Virtual Environment in Working Directory (Windows) #
# ========================================================== #

# Go to installation directory.
cd $install_dir

# Check if virtual environment already exists.
# -d : directory exists
if [ -d "venv" ]; then
    # Would you like to remove the venv?
    while true; do
        read -p "The 'venv/' folder already exists. Would you like to overwrite it? (y/n)" yn
        case $yn in
            [Yy]* )
                echo "Removing 'venv/' folder..."
                rm -rf ./venv/
                echo "Creating the virtual environment under the 'venv' folder..."
                python -m venv ./venv/
                break;;
            [Nn]* ) break;;
        esac
    done
else
    echo "Creating the virtual environment under the 'venv' folder..."
    python -m venv ./venv/
fi

# Add '..' folder to Python path.
ADD_PARDIR=false
if [ "$ADD_PARDIR" = true ]; then
    # Source: https://www.mkssoftware.com/docs/man1/realpath.1.asp
    # realpath .. &> ./venv/Lib/site-packages/_global_path.pth
    echo "import _global_path" &> ./venv/Lib/site-packages/_global_path.pth
    _realpath=$(realpath ..)
    _drive_upper=$(echo ${_realpath:1:1} | tr a-z A-Z)
    _windows_path="$_drive_upper:${_realpath:2}"
    _windows_backslash=${_windows_path//\//\\\\} # https://unix.stackexchange.com/a/589316
    echo "Adding $_windows_backslash to venv .pth file."
    echo "import site; site.addsitedir(r'$_windows_backslash')" &> ./venv/Lib/site-packages/_global_path.py
fi


# Activate virtual environment and install the required packages.
echo "Installing the required Python packages... This may take a while."
source venv/Scripts/activate
pip3 install -r requirements.txt

# Deactivate (close) the virtual environment.
# This function is defined when the activate file is called.
# See: https://stackoverflow.com/a/990779
deactivate

# Let the user know we are finished.
echo "Finished. You can activate the virtual environment by running the following:"
echo "source venv/Scripts/activate"

# Restore original working directory.
cd $original_working_dir
