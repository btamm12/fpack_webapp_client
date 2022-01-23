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

# * 1.2. Install the required Linux packages.
echo "> Installing required Linux packages."
source linux_packages/install_packages.sh

# * 1.3. Create symlink for create_venv.sh.
echo "> Creating 'create_venv.sh' symlink in root directory."
source ../common/create_venv/create_venv_symlink.sh

# * 1.4. Create "my_sections.txt".
echo "> Creating 'my_sections.txt' file in collaboration directory."
source ../common/my_sections/create_my_sections.sh

# * 1.5. Create venv.
echo "> Creating venv..."
source ../../create_venv.sh

# 2. Install development components?

# Would you like to install the developer components?
while true; do
    read -p "Would you like to install the developer components (i.e. VSCode installation scripts)? (y/n)" yn
    case $yn in
        [Yy]* )
            break;;
        [Nn]* )
            echo "Installation finished."
            cd $original_working_dir
            exit 0
            break;;
    esac
done

echo "Installing developer components..."

# * 2.1. Check if VSCode is installed.
echo "> Checking VSCode installation."
code_installed=false
command -v code >/dev/null 2>&1 && code_installed=true
if [ "$code_installed" = false ] ; then
    echo 'code is not installed! Please install this first before continuing.'
    echo 'Method 1: Normal installation (.deb)'
    echo 'Method 2: Portable installation (extract .tar.gz)'
    echo 'Download page: https://code.visualstudio.com/download'
    cd $original_working_dir
    exit 1
fi


# * 2.2. Create the correct launch.json symlink.
echo "> Creating 'launch.json' symlink in .vscode folder."
source ../common/dev/vscode_launch/create_launch_symlink.sh

# * 2.3. Install the recommended VSCode extensions.
echo "> Installing the recommended VSCode extensions."
source ../common/dev/vscode_extensions/install_extensions.sh

# Restore original working directory.
cd $original_working_dir