# Planned Changes

# Planned Changes

## `0.1.2`

**Title:** Patch 0.1.2 \
**Release Date:** N/A

### Added
- **Finished:**
  - add hyperlink to audio file when user finishes transcript
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
  - Fix this exception:
    ```
    Traceback (most recent call last):
      File "D:\Windows\GitHub\test\fpack_webapp_client\src\model\manager.py", line 501, in _extract_section_segments
        await converter.write_textgrids_async(
      File "D:\Windows\GitHub\test\fpack_webapp_client\src\utils\ctm_converter.py", line 310, in write_textgrids_async
        utt_tier = textgrid.IntervalTier(
      File "D:\Windows\GitHub\test\fpack_webapp_client\venv\lib\site-packages\praatio\data_classes\interval_tier.py", line 57, in __init__
        raise errors.TextgridStateError(
    praatio.utilities.errors.TextgridStateError: The start time of an interval (20.53933) cannot occur after its end time (20.53933)
    ```

### Security
- **Finished:**
  - ...
- **Work In Progress:**
  - ...
- **To-Do:**
  -  ...


## `0.1.3`

**Title:** Patch 0.1.3 \
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
  - Instead of using round() everywhere in CtmLine and CtmConverter (to avoid
    praatio's warnings of "start cannot exceed end" when the difference is due to
    extremely small floating point addition errors), we should change the sensitive
    parts with more of a clamp function.
    ```

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

