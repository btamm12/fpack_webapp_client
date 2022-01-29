[\[Back\]](./README.md) \
🔲🔲🔲⏹⬛️⬛️⬛️⬛️ \
[\[<---\]](./03_working_with_praat.md) [\[--->\]](./05_request_subject_mapping.md)

# 4. Your Task As Annotator

## 4.1. Workflow

### 4.1.1. Step 1: Annotate Me!

This following directory will be automatically filled with a number of annotation
files that were generated using the ASR model.
```
fpack_webapp_client/data/01_annotate_me/
```
Your job is to load these files into Praat, correct the annotations, and save the
results in the `02_corrected_textgrids/` directory.

**Note 1:** if the annotation file is not yet finished, but you would like to save
your progress, then you should overwrite the file in the `01_annotate_me/` folder.

**Note 2:** if the annotation file is too difficult and you would like to save it for
later, then you should save the file in the `difficult_to_annotate/` folder.

*See the [README](../data/01_annotate_me/README.md) in `01_annotate_me/` for more
details about how exactly the Praat annotation software should be used.*


### 4.1.2. Step 2: Corrected TextGrids

*There's no work for you to do.* Just save the finished annotation files in the
following folder.
```
fpack_webapp_client/data/02_corrected_textgrids/
``` 

After you finish an entire interview section, the TextGrid files that you saved in
this folder will be automatically converted into a transcription `.txt` file, which
will be saved in the `03_generated_transcripts/` directory.

### 4.1.3. Step 3: Automatically Generated Transcripts

As mentioned above, the automatically generated transcripts will appear in the
following folder as `.txt` files.
```
fpack_webapp_client/data/03_generated_transcripts/
```
You should submit them to me in batches, so I can upload them to the server.

*See [Section 7](07_sending_your_results.md) for more details about how to submit the
transcripts.*


### 4.1.4. Step 4: Submitted Transcripts

In order to keep the process organized and streamlined, the submitted transcripts
should be moved to the following folder.
```
fpack_webapp_client/data/04_submitted_transcripts/
```

## 4.2. Annotation Rules

The language spoken by the participants is Dutch. We will therefore make use of the
"Protocol for Orthographic Transcription" for Dutch.

The protocol is detailed, and to make easier for the later NLP analysis, we will not
include all of the rules. The selected rules are listed in the [protocol
README](protocol/README.md). Read these in detail before starting the annotations!


## 4.3. Annotation Example

It may be useful to see the tool in action, so I have created a video in which
a part of the interview section is annotated.

If you click the image below, it will take you to that video. The duration is 9 minutes.

**EXAMPLE VIDEO:**

[![Annotation Example](https://img.youtube.com/vi/9HJH_Uqo1FA/0.jpg)](https://youtu.be/9HJH_Uqo1FA)
