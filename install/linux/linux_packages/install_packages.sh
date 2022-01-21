#!/bin/bash

# Directory containing Bash script, i.e. "install/linux/linux_packages/".
script_dir="$(dirname $(realpath "${BASH_SOURCE[0]}"))"
# Original working directory.
original_working_dir=$PWD

# Move to script directory.
cd $script_dir

# Get package list "pkg1 pkg2 ...".
packages=""
for pkg in $(cat packages.txt); do 
   packages="$packages $pkg"
done

echo "The following Linux packages will be installed: ${packages}"

# Install packages. Answer "yes" to all with `-y` flag.
sudo apt install $packages -y

# Restore original working directory.
cd $original_working_dir