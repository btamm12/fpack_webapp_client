# Changelog - Versions 0.x.x

All notable changes to this project will be documented in this file.

Group the changelog under the following headers for each release.
- **Added:** for new features
- **Changed:** for changes in existing functionality
- **Deprecated:** for soon-to-be removed features
- **Removed:** for now removed features
- **Fixed:** for any bug fixes
- **Security:** in case of vulnerabilities

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## `0.2.0`

**Title:** v0.2.0 \
**Release Date:** 2022-01-30

### Added
- Added review feature. Annotators are automatically assigned certain submitted
  transcripts to review.

### Changed
- Bumped version to 0.2.0

### Fixed
- Improved CtmLine and CtmConverter, not using round() anymore but checking
  floating point rounding errors properly.


## `0.1.2`

**Title:** Patch 0.1.2 \
**Release Date:** 2022-01-28

### Added
- added hyperlink to audio file when user finishes transcript
- added bump version in planned_changes template

### Changed
- bumped version to v0.1.2

### Fixed
- Fixed an error where final end_context interval (which should not exist) was trying
  to be created. praatio did not like the fact that the interval start time was
  equal to the TextGrid max time. This ended up being a small rounding error.


## `v0.1.1`

**Title:** Patch v0.1.1 \
**Release Date:** 2022-01-28


### Added
- Created changelog. This can be found in the `docs/changelog/` folder.
- Created version checker (latest version hosted on server).
- Providing 4 seconds of left- and right-context to make annotating the edges easier.
- Added example_transcripts in `data/` directory. This will automatically download
  example transcript files and a hyperlink to the audio file when the application is
  run. 

### Changed
- Bumped version number to `0.1.1`.

### Fixed
- Fix how special charaters, (e.g. "è") are loading from CTM file.


## `v0.1.0`

**Title:** Initial Release \
**Release Date:** 2022-01-24

### Added
- Client side:
  - Created Python tool to speed up speech-to-text annotations using Praat.
  - Created `Sanic` application that will run while the client is annotating in
    Praat.
  - Created simple logger.
  - Created `Manager` class which is responsible for the application logic.
  - Created `State` class which is responsible for storing data that needs to be
    remembered after the application is closed.
  - Created utility functions/classes `CtmConverter`, `CtmLine` and
    `textgrid_to_utterance()` to help with conversions between file types.
- Server side:
  - Created static website `https://homes.esat.kuleuven.be/~btamm/fpack_webapp/v0/`,
    which hosts WAV/CTM files for the first 21 participants.
  - The client must know the "subject mapping" in order to access files.
- Created documentation: 
  - main `README.md` - get project up and running ASAP.
  - `collaboration/` folder - how to choose which sections you will annotate.
  - `docs/` folder - general documentation.
  - `data/` folder - specific documentation for using the tool.
  - `install/` folder - installation instructions for Linux/Windows.
  - `src/` folder - short explanation of how the code works.
- Defined annotation protocol based on the "Protocol for Orthographic Transcription".
  This can be found in the `docs/protocol/` folder.
