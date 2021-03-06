[\[Back\]](./README.md) \
🔲⏹⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \
[\[<---\]](./01_overview.md) [\[--->\]](./03_working_with_praat.md)

# 2. File Types

## 2.1. Introduction

You will be working with two types of files:
1. audio segments
2. TextGrids

## 2.2. Audio Segments
Each interview consists of multiple **sections**. The names of the sections are
listed below.
- `actua`
- `bio_part[1-5]`
- `day`
- `object`
- `picture`

Each of these interview sections is recorded as a separate audio file. Most of the
interview sections are relatively short (1-5 minutes), but there is one section
(`object`) that is long (10-15 minutes).

To make your life easier, every audio file will be split into **audio segments**
containing roughly 15 seconds of audio. The name of these files are:
```
sXXX_[type]_BL_XXX.wav
```
where `X` is an arbitrary number and `[type]` is the name of the interview
section.

## 2.3. TextGrids
Annotations are stored as **TextGrid** files, which contain the transcript along with
the timing of each word (i.e. when does the word start/stop).

Instead of having you, the annotator, indicate the start/stop times and transcribe
each word manually, we are using Automatic Speech Recognition (ASR) to speed up the
process. The ASR model will generate a `.ctm` file containing the predicted
transcript (and timing) of the audio file. This application will use the `.ctm` file
to generate an initial TextGrid file.

There is one TextGrid file per audio segment, namely:
```
sXXX_[type]_BL_XXX.TextGrid
```
The meaning of `X` and `[type]` is the same as above.