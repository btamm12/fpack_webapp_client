# Installation (Linux)

## 1. GitHub (First-Time Setup)

Only follow this part if you have not used Git and GitHub before.

### 1.1 Install Git

```
apt-get install git
```

### 1.2. Register SSH Key
If you already have an SSH key registered in GitHub for your computer, you may skip
this step. If you don't, you need to follow this step in order to clone the
repository.

1. Open a web browser and navigate to https://github.com/settings/keys.
2. Click the "New SSH Key" button.
3. Check if you already have an SSH key on your computer. You should find it in the
   following location.
   ```
   ~/.ssh/id_rsa.pub
   ```
   If this file exists, **skip to step 5**.
4. Time to generate a new SSH key.
   - Open a terminal and run the following command.
     It is best to use the same email that you used to register for GitHub.
     ```
     ssh-keygen -t rsa -b 4096 -C "[YOUR.EMAIL@EXAMPLE.COM]"
     ```
   - The script will ask you to name the file. Leave this blank and press Enter.
   - The script will ask you to set a password. Leave this blank and press Enter.
   - The script will ask you to confirm your password. Leave this blank and press
     Enter.
5. Copy the contents of `~/.ssh/id_rsa.pub` and paste it in the "Key" section of the
   webpage. Enter a title, e.g. "Lenovo-Laptop-Linux", and click the "Add SSH Key"
   button.

### 1.3. Configure Git Username/Email

Configure your username and email in order to push to GitHub. It is best to use the
same email that you used to register for GitHub.
```
git config --global user.name "[username]"
git config --global user.email "[email]"
```

## 2. Clone Repository

Use the following command to clone the repository.

**Note: the argument `-c core.symlinks=true` is crucial for pushing/pulling symlinks!**

```
git clone -c core.symlinks=true git@github.com:btamm12/fpack_webapp_client.git
```

## 3. Installation Script

```
cd install/linux
./install_linux.sh
```

Use the command above to install the **required components**.
- Linux packages (see [packages.txt](linux_packages/packages.txt))
- Creating `create_venv.sh` symlink in root directory
- Creating `my_sections.txt` in collaboration directory

The script will also ask if you want to install the **development components**. This
requires the installation of [VSCode](https://code.visualstudio.com/download).
The development components include
- Creating `launch.json` symlink in .vscode directory
- Installing recommended VSCode extensions (see [extensions.txt](../common/dev/vscode_extensions/extensions.txt))

