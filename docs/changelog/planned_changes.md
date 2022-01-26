# Planned Changes

## `v0.1.1`

**Title:** - \
**Release Date:** N/A


### Added
- **Finished:**
  - Created changelog. This can be found in the `docs/changelog/` folder.
- **Work In Progress:**
  - use version checker (latest version hosted on public_html/)
- **To-Do:**
  - provide left/right context with specific tags (1-2 seconds)
    - EDIT: maybe ~3 seconds cause it's hard to tell if it's the end of the sentence
    - of course at start/end of audio, this is not possible
    - the annotation of this context is [CONTEXT FROM NEXT/PREV SEGMENT! DO NOT
      ANNOTATE]
    - the context annotation tag should not be loaded into the transcript .txt file
    - there's not a good way to prevent the user from changing the context annotation,
      just give a warning "MISSING CONTEXT ANNOTATION '[CONTEXT FROM NEXT/PREV SEGMENT!
      DO NOT ANNOTATE]' AT END/BEGINNING OF TextGrid FILE XXX.TextGrid! PLS FIX"
  - add example_transcripts (s92 stored on GitHub, as soon as mapping available, fetch
    example from server)


### Changed
- **Finished:**
  - ...
- **Work In Progress:**
  - ...
- **To-Do:**
  -  ...

### Deprecated
- **Finished:**
  - ...
- **Work In Progress:**
  - ...
- **To-Do:**
  -  ...

### Removed
- **Finished:**
  - ...
- **Work In Progress:**
  - ...
- **To-Do:**
  -  ...

### Fixed
- **Finished:**
  - ...
- **Work In Progress:**
  - ...
- **To-Do:**
  - fix how special charaters, e.g. "è" are loading from CTM file

### Security
- **Finished:**
  - ...
- **Work In Progress:**
  - ...
- **To-Do:**
  -  ...



## `v1.0.0`

**Title:** - \
**Release Date:** N/A


### Added
- **Finished:**
  - ...
- **Work In Progress:**
  - ...
- **To-Do:**
  - ...

### Changed
- **Finished:**
  - ...
- **Work In Progress:**
  - ...
- **To-Do:**
  - Create server URL with `v1` instead of `v0`.
  - Change server data symlink from
    ```
    ~/public_html/fpack_webapp/v0/data/fpack --> ~/data/live/fpack/v0/
    ```
    to
    ```
    ~/public_html/fpack_webapp/v1/data --> ~/data/live/fpack/v1/
    ```
    i.e. why do we need to specify in the URL twice that we want F-PACK data?
    ```python
    # Old URL.
    AUDIO_URL = "https://homes.esat.kuleuven.be/~btamm/fpack_webapp/v0/data/fpack/audio"
    # New URL.
    AUDIO_URL = "https://homes.esat.kuleuven.be/~btamm/fpack_webapp/v1/data/audio"
    ```

### Deprecated
- **Finished:**
  - ...
- **Work In Progress:**
  - ...
- **To-Do:**
  -  ...

### Removed
- **Finished:**
  - ...
- **Work In Progress:**
  - ...
- **To-Do:**
  -  ...

### Fixed
- **Finished:**
  - ...
- **Work In Progress:**
  - ...
- **To-Do:**
  - fix how special charaters, e.g. "è" are loading from CTM file

### Security
- **Finished:**
  - ...
- **Work In Progress:**
  - ...
- **To-Do:**
  -  ...

