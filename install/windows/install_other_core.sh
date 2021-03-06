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

# 1. Install other core components.

echo "Installing other core components..."

# * 1.1. Create symlink for create_venv.sh.
echo "> Creating 'create_venv.sh' symlink in root directory."
source ../common/create_venv/create_venv_symlink.sh

# * 1.2. Create "my_name.txt" and "my_sections.txt"
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