# Installation (Linux)

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
bash install_linux.sh
```

Use the command above to install the **required components**.
- Linux packages (see [packages.txt](linux_packages/packages.txt))
- Creating `create_venv.sh` symlink in root directory
- Creating `my_name.txt` in collaboration directory
- Creating `my_sections.txt` in collaboration directory
- Creating the virtual environment in the root directory
