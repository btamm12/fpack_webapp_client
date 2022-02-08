# Planned Changes

## `v0.2.1`

**Title:** Punctuation Generation \
**Release Date:** N/A


### Added
- **Finished:**
  - Added punctuation generation (only ".") using heuristic method
- **Work In Progress:**
  - ...
- **To-Do:**
  - ...

### Changed
- **Finished:**
  - bump version to v0.2.1
- **Work In Progress:**
  - ...
- **To-Do:**
  - ...

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
  - ...

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
  - bump version to v1.0.0
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
  - ...

### Security
- **Finished:**
  - ...
- **Work In Progress:**
  - ...
- **To-Do:**
  -  ...

