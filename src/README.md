# Source Code

**It is only necessary to read this if you are a developer.**

This README explains how most of the source code works.

## 1. Application

The entry point of the application is the file `src/app.py`.

This file will
- create the Sanic application
- create the `Manager` object (contains logic, performs operations)
- create the logger object
- start a periodic task to call the `Manager.tick()` function every `X` seconds.

## 2. State

The application state is saved in the location `src/state.pkl`.

**It contains information about which interview sections have been
downloaded/extracted**. This way, the application remembers its state if it is
restarted.

The rest of the logic happens reactively, which does not need to be saved in the
state. For example:
```
IF:   TextGrid file detected in 02_corrected_textgrids/
THEN: move corresponding WAV to 02_corrected_textgrids/
```



## 3. Modules

### 3.1. Logger

The logger code is quite simple and can be found in `src/logger/`.

### 3.2. Model

The model can be found in `src/model/` and consists of two files:
- `manager.py`
- `state.py`

**3.2.1. Manager**

The `Manager` class contains all of the logic of the application.

Every `X` seconds, the manager will perform 3 checks.

1. Check if new data needs to be downloaded. \
   If so, it will...
   - download the CTM/WAV files for the next interview section;
   - extract 15-second segments and place the segment TextGrid/WAV files in the
     `01_annotate_me/` folder.
2. Check if there are any new TextGrid files in `02_corrected_textgrids/`. \
   If so, it will ...
   - move the corresponding WAV file from `01_annotate_me/` to
     `02_corrected_textgrids/`;
   - delete the old TextGrid file from `01_annotate_me/`.

   ( The same logic applies for TextGrid files saved in `difficult_to_annotate/` )
3. Check if there are any interview sections where all files have been moved to
   `02_corrected_textgrids/`, i.e. that the annotator has finished the section. \
   If so, it will...
    - generate the transcript `.txt` file in `03_generated_transcripts/`;
    - delete the segment WAV/TextGrid files from `02_corrected_textgrids/`.

**3.2.2. State**

As explained above, the `State` class contains information about which interview
sections have been downloaded/extracted. This way, the application remembers its
state if it is restarted.

## 3.3. Utilities

The utility functions can be found in `src/utils/`. These include:
- A `CtmConverter` class to convert a CTM/WAV file pair into a number of
  TextGrid/audio segments.
- A `CtmLine` class which represents one line in the CTM file.
- A `textgrid_to_utterance()` function which will convert a number of TextGrid
  segment files into a single transcript `.txt` file.