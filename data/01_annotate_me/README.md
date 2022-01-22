# Step 1: Annotate Me!

This directory will be automatically filled with a number of files. Your job is
to load these files into Praat, correct the annotations, and save the results in
the `02_corrected_textgrids/` directory.

## 1.1. Load Files Into Praat

**Loading TextGrid + WAV File:**
> 1. In the Objects window, select  \
>    `Open` > `Read from file...`
> 2. Navigate to the `01_annotate_me/` folder.
> 3. Highlight the corresponding `.TextGrid` and `.wav` file.
> 4. Press the `Open` button.



https://user-images.githubusercontent.com/32679237/150639398-970bfc8c-6205-4a50-8e60-29c356b9cec6.mp4





(insert gif: load `xyz.wav` and `xyz.TextGrid` into object window, select both and press view)

## 1.2. Correcting Annotations


(insert gif: correct mistake in )

**Important Notes:**
- Corrections only need to be made in the "words" tier. Any modification in the
  "utterance" and "score" tier will be overwritten by a later process, so there
  is no point in making modifications there.
- Only the final word order matters!
- Feel free to
  - replace a word, e.g.
    ```
    | vormde |  ⟶  | vormden |
    |  0.95  |     |  0.95   |
    ```
  - remove a word by replacing it with a blank string, e.g.
    ```
    | het | was | al  | goed |  ⟶   | het | was |     | goed |
    | 0.8 | 0.8 | 0.6 | 0.95 |  ⟶   | 0.8 | 0.8 | 0.6 | 0.95 |
    ```
  - remove any boundaries (`Alt+Backspace`), e.g.
    ```
    | dag | tien |  ⟶  |  dachten  |
    | 0.7 |  0.6 |     | 0.7 | 0.6 |
    ```
  - have two or more words in a single interval e.g.
    ```
    | of  | Zwitsal | begonnen |  ⟶  | of  | is het al | begonnen |
    | 0.8 |   0.5   |   0.95   |  ⟶  | 0.8 |    0.5    |   0.95   |
    ```

## 1.3. Saving Results

When you have completely corrected the annotation file, save it in the
`02_corrected_textgrids/` folder, using the same file name.

**Saving A TextGrid File:**
> 1. In the TextGrid editor window, select \
>    `File` > `Save TextGrid as text file...`
> 2. Navigate to the `02_corrected_textgrids/` folder.
> 3. Press the `Save` button (don't change the file name).

(insert gif: save result as `xyz.TextGrid` in `02_corrected_textgrids/` folder)

**Note:** if the annotation file is not yet finished, but you would like to save
your progress, then you should overwrite the file (i.e. save it in the
`01_annotate_me/` folder).

### 1.1.1. File Types

There are two types of files:
1. audio segments
2. TextGrids

Each interview is recorded over multiple audio files. To make your life easier,
every audio file (duration = 1-15 minutes) will be split into **audio segments**
containing roughly 15 seconds of audio. The name of these files are:
```
sXXX_[type]_BL_XXX.wav
```
where `X` is an arbitrary number and `[type]` is the name of the interview
section, i.e. one of the following:
- `actua`
- `bio_part[1-5]`
- `day`
- `object`
- `picture`

The annotation is stored as a **TextGrid** file, which contains the
transcription along with the timing of each word (i.e. when does the word
start/stop).

Instead of having you, the annotator, indicate the start/stop times and
transcribe each word manually, we are using Automatic Speech Recognition (ASR)
to speed up the process. The ASR model will generate an initial transcription
(and timing) from the audio file, and this application will use the
transcription to generate an initial TextGrid file.

There is one TextGrid file per audio segment, namely:
```
sXXX_[type]_BL_XXX.TextGrid
```

## 1.2. What To Do?

