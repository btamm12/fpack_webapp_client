# F-PACK Web App - Client

## 1. Overview

### 1.1. Project Description

This annotation process is part of a longitudinal study of elderly subjects over 10
years to study the evolution of Alzheimer's disease and how it relates to speech and
brain characteristics. Some of the participants will be completely healthy, while
others will have a diagnosis of an early-stage neurodegenerative disease. The
language spoken by the participants is Dutch.

Spontaneous speech data is already being collected through interviews. This data must
be accurately transcribed in order to perform further Natural Language Processing
(NLP) analysis.

### 1.2. Speech-To-Text Transcription Tool

This tool uses the power of Automatic Speech Recognition (ASR) to greatly decrease
the amount of time needed to transcribe audio files. The tool also uses a streamlined
process to keep your annotations organized.


**Video:**

https://user-images.githubusercontent.com/32679237/150655652-c79109e7-2384-49a3-83ec-1c590af279c8.mp4

**Highlights:**

- **Automatic data loading:** unannotated files are automatically downloaded from the
  server and placed in your working directory (`data/01_annotate_me`).
- **Data segmentation:** instead of working with the entire audio file, this tool
  will split the interview into segments that are roughly 15 seconds long. This way
  each segment is manageable, and there's never a risk of losing too much progress
  (e.g. if you forget to save or your computer crashes).
- **Transcription prediction:** instead of having you, the annotator, indicate the
  start/stop times and transcribe each word manually, we are using Automatic Speech
  Recognition (ASR) to speed up the process. An ASR model will be used to
  automatically generate a transcription and it will be your job to fix any mistakes.

## 2. Installation

### 2.1. Clone Repository

You should download the repository by running one of the following commands in a
terminal (Linux) or in Git Bash (Windows).

**Note: the argument `-c core.symlinks=true` is crucial for pushing/pulling
symlinks!**

*Annotator*
```
git clone -c core.symlinks=true https://github.com/btamm12/fpack_webapp_client.git
```

*Developer (Linux)*
```
git clone -c core.symlinks=true git@github.com:btamm12/fpack_webapp_client.git
```

*Developer (Windows)*
```
git clone -c core.symlinks=true git@github.com:btamm12/fpack_webapp_client.git
git config --global core.autocrlf true
```

### 2.2. Full Installation Instructions

Please follow the appropriate guide based on your operating system.

*Annotator*
- [Linux Installation (Annotator)](install/linux/install_linux.md)
- [Windows Installation (Annotator)](install/windows/install_windows.md)

*Developer*
- [Linux Installation (Developer)](install/linux/install_linux_dev.md)
- [Windows Installation (Developer)](install/windows/install_windows_dev.md)


## 3. Documentation

It is highly recommended to read the documentation before starting the annotations.

- [Documentation](docs/README.md)

There is also more specific details available in the `data/` folder, where most of
your time will be spent.

- [Specific Details (Data Folder)](data/README.md)
## 4. Request Subject Mapping

Before this application can do anything, it needs a certain file, called the "subject
mapping". This file provides an extra layer of security to protect the data of the
study participants.

**To get access to this file, you must send me an email.** Please mention "subject
mapping" in the email subject.
```
bastiaan.tamm@kuleuven.be
```

When I send you the file `subject_mapping.txt`, you must place it in the root folder
of the repository, i.e.
```
fpack_webapp_client/subject_mapping.txt
```

## 5. Choosing Your Interview Sections

You should coordinate with your fellow annotators about who will annotate which data.
Otherwise you might both annotate the same interviews, which would not be a great use
of time!

**You must select some interview sections before the tool will start working.** See
the collaboration folder for more details.

- [Collaboration Folder](collaboration/README.md)

## 6. Running The Tool

To run the tool, you must run the following commands in a terminal (Linux) or in Git
Bash (Windows).

### 6.1. Activate The Virtual Environment

*Linux*
```
cd fpack_webapp_client/
source venv/bin/activate
```

*Windows*
```
cd fpack_webapp_client/
source venv/Scripts/activate
```

**Note:** the virtual environment can be deactivated by entering the `deactivate`
command.

### 6.2. Run The Application
*Linux*
```
python3 src/app.py
```

*Windows*
```
python src/app.py
```
