# Installation – Annotator (Linux)

## 1. Install Praat

Praat is the software we will use for creating the annotations. To install Praat, run
```
sudo apt-get install praat
```
or you can download the `.tar.gz` file from the
[website](https://www.fon.hum.uva.nl/praat/download_linux.html).


## 2. Install Git

Git comes included with many Linux distributions. If you already have Git installed,
you can skip this section.

To install Git, run
```
apt-get install git
```
or you can follow the instructions on the
[website](https://git-scm.com/download/linux) for non-Debian distributions.

## 3. Clone Repository

Use the following commands to clone the repository.

**Note: the argument `-c core.symlinks=true` is crucial for pushing/pulling symlinks!**

```
git clone -c core.symlinks=true https://github.com/btamm12/fpack_webapp_client.git
```

## 4. Installation Script

```
cd install/linux
./install_linux.sh
```

Use the command above to install the **required components**.
- Linux packages (see [packages.txt](linux_packages/packages.txt))
- Creating `create_venv.sh` symlink in root directory
- Creating `my_sections.txt` in collaboration directory

The script will also ask if you want to install the **development components**.
- *Enter "n" to not install these components.*
