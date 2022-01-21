#!/bin/bash

# Directory where virtual environment will be installed, i.e. root directory.
install_dir="$(realpath $(dirname "${BASH_SOURCE[0]}"))"
# Original working directory.
original_working_dir=$PWD

# ======================================================== #
# Install Virtual Environment in Working Directory (Linux) #
# ======================================================== #

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
                python3 -m venv ./venv/
                break;;
            [Nn]* ) break;;
        esac
    done
else
    echo "Creating the virtual environment under the 'venv' folder..."
    python3 -m venv ./venv/
fi

# Add '..' folder to Python path.
ADD_PARDIR=false
if [ "$ADD_PARDIR" = true ]; then
    python_dirs=$(ls -d ./venv/lib/python*)
    echo "Adding $(realpath ..) to venv .pth file."
    realpath .. &> ${python_dirs[0]}/site-packages/_global_path.pth
fi


# Activate virtual environment and install the required packages.
echo "Installing the required Python packages... This may take a while."
source venv/bin/activate
pip3 install -r requirements.txt

# Deactivate (close) the virtual environment.
# This function is defined when the activate file is called.
# See: https://stackoverflow.com/a/990779
deactivate

# Let the user know we are finished.
echo "Finished. You can activate the virtual environment by running the following:"
echo "source venv/bin/activate"

# Restore original working directory.
cd $original_working_dir
