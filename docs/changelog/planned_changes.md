# Planned Changes


## `v0.1.1`

**Title:** ? \
**Release Date:** ?

### Added
- /

### To Add
- provide left/right context with specific tags (1-2 seconds)
  - EDIT: maybe ~3 seconds cause it's hard to tell if it's the end of the sentence
  - of course at start/end of audio, this is not possible
  - the annotation of this context is [CONTEXT FROM NEXT/PREV SEGMENT! DO NOT
    ANNOTATE]
  - the context annotation tag should not be loaded into the transcript .txt file
  - there's not a good way to prevent the user from changing the context annotation,
    just give a warning "MISSING CONTEXT ANNOTATION '[CONTEXT FROM NEXT/PREV SEGMENT!
    DO NOT ANNOTATE]' AT END/BEGINNING OF TextGrid FILE XXX.TextGrid! PLS FIX"
- use version checker (latest version hosted on public_html/)
- add example_transcripts (s92 stored on GitHub, as soon as mapping available, fetch
  example from server)

### Changed
- /

### To Change
- fix how special charaters, e.g. "è" are loading from CTM file
