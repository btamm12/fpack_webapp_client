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

# * 1.2. Create "my_name.txt".
echo "> Creating 'my_name.txt' file in collaboration directory."
source ../common/my_name/create_my_name.sh

# * 1.3. Create "my_sections.txt".
echo "> Creating 'my_sections.txt' file in collaboration directory."
source ../common/my_sections/create_my_sections.sh

# * 1.4. Create venv.
echo "> Creating venv..."
source ../../create_venv.sh

# Restore original working directory.
cd $original_working_dir