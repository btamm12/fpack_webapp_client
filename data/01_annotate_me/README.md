# Step 1: Annotate Me!

This directory will be automatically filled with a number of files. Your job is to
load these files into Praat, correct the annotations, and save the results in the
`02_corrected_textgrids/` directory.

## 1.1. Load Files Into Praat

**Loading TextGrid + WAV File:**
> 1. In the Objects window, select  \
>    `Open` > `Read from file...`
> 2. Navigate to the `01_annotate_me/` folder.
> 3. Highlight the corresponding `.TextGrid` and `.wav` file.
> 4. Press the `Open` button.

**Video:**

https://user-images.githubusercontent.com/32679237/150639398-970bfc8c-6205-4a50-8e60-29c356b9cec6.mp4



## 1.2. Correcting Annotations

**Video:**

https://user-images.githubusercontent.com/32679237/150655652-c79109e7-2384-49a3-83ec-1c590af279c8.mp4

**Important Notes:**
- Corrections only need to be made in the "words" tier. Any modification in the
  "utterance" and "score" tier will be overwritten by a later process, so there is no
  point in making modifications there.
- Only the final word order matters! Feel free to
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
  - remove any boundaries (shortcut `Alt+Backspace`), e.g.
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

**Video:**

https://user-images.githubusercontent.com/32679237/150655656-3a47c8ce-c38f-4c80-9ba5-3fbcac5c39b6.mp4

**Note 1:** if the annotation file is not yet finished, but you would like to save
your progress, then you should overwrite the TextGrid file (i.e. save it in the
`01_annotate_me/` folder).

**Note 2:** if the annotation file is too difficult and you would like to save it for
later, then you should save the TextGrid file in the `difficult_to_annotate/` folder.
