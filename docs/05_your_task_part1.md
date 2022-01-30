[\[Back\]](./README.md) \
🔲🔲🔲🔲⏹⬛️⬛️⬛️⬛️ \
[\[<---\]](./04_request_subject_mapping.md) [\[--->\]](./06_your_task_part2.md)

# 5. Your Task (Part 1)

Your task as an annotator consists of two parts:
- **part 1: annotating**
- part 2: reviewing

This section covers the first part of your task.

## 5.1. Annotation Workflow

### 5.1.1. Step 1: Annotate Me!

The following directory will be automatically filled with a number of annotation
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


### 5.1.2. Step 2: Corrected TextGrids

*There's no work for you to do.* Just save the finished annotation files in the
following folder.
```
fpack_webapp_client/data/02_corrected_textgrids/
``` 

After you finish an entire interview section, the TextGrid files that you saved in
this folder will be automatically converted into a transcript `.txt` file, which will
be saved in the `03_generated_transcripts/` directory.

### 5.1.3. Step 3: Automatically Generated Transcripts

As mentioned above, the automatically generated transcripts will appear in the
following folder as `.txt` files.
```
fpack_webapp_client/data/03_generated_transcripts/
```
You should submit them to me in batches, so I can upload them to the server.

*See [Section 8](08_sending_your_results.md) for more details about how to submit the
transcripts.*


### 5.1.4. Step 4: Submitted Transcripts

In order to keep the process organized and streamlined, the submitted transcripts
should be moved to the following folder.
```
fpack_webapp_client/data/04_submitted_transcripts/
```

## 5.2. Annotation Rules

The language spoken by the participants is Dutch. We will therefore make use of the
"Protocol for Orthographic Transcription" for Dutch.

The protocol is detailed, and to make easier for the later NLP analysis, we will not
include all of the rules. The selected rules are listed in the [protocol
README](protocol/README.md).

**Please read this in detail before starting the annotations!**


## 5.3. Annotation Example

It may be useful to see the tool in action, so I have created a video in which a part
of the interview section is annotated.

If you click the image below, it will take you to that video. The duration is 9
minutes.

**EXAMPLE VIDEO:**

[![Annotation Example](https://img.youtube.com/vi/9HJH_Uqo1FA/0.jpg)](https://youtu.be/9HJH_Uqo1FA)
