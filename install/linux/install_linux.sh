# Install (Linux)

# Save script directory and working directory.
# Source: https://stackoverflow.com/a/10348989
# Example: https://stackoverflow.com/a/55798664

# Directory containing Bash script, i.e. "install/linux/".
script_dir="$(dirname $(realpath "${BASH_SOURCE[0]}"))"
# Original working directory.
original_working_dir=$PWD

# Move to script directory.
cd $script_dir

# 1. Install core components.

echo "Installing core components..."

# * 1.1. Check if Python is installed.
#        Source: https://stackoverflow.com/a/38485534
echo "> Checking Python installation."
python_installed=false
command -v python3 >/dev/null 2>&1 && python_installed=true
if [ "$python_installed" = false ] ; then
    echo 'python3 is not installed! Please install this first before continuing.'
    echo 'See: https://docs.python-guide.org/starting/install3/linux/'
    cd $original_working_dir
    exit 1
fi

# * 1.2. Create "my_name.txt" and "my_sections.txt".
echo "> Creating 'my_name.txt' and 'my_sections' file in collaboration directory."
cd ../../collaboration
touch "my_name.txt"
touch "my_sections.txt"

# * 1.3. Create venv.
echo "> Creating venv..."
cd ../..
make create_environment

# Restore original working directory.
cd $original_working_dir