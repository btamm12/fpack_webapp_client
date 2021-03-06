# Changelog - Versions 1.x.x

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

## `v1.0.2`

**Title:** Small patch v1.0.2 \
**Release Date:** 2022-05-11

### Changed
- Bumped version to v1.0.2

### Fixed
- Stripping new line character from server version file.

## `v1.0.1`

**Title:** Fixed overwriting existing transcripts in v1.0.1 \
**Release Date:** 2022-05-11

### Changed
- After the user finishes all segments, the program will generate a single transcript
  .txt file (just as before). If there is a conflict, the program will now search for
  a unique name instead of overwriting the previous transcript. This will prevent any
  data loss.
- Bumped version to v1.0.1

## `v1.0.0`

**Title:** New installation procedure in v1 \
**Release Date:** 2022-03-11

Note that a migration is needed to upgrade to `v1`. Please refer in the [migration_v1
document](../migration/migration_v1.md) for this.

### Changed
- Using more simple installation procedure
  - Changed server URL from `v0` to `v1`. Note that the underlying data is the same
    through the `v1` API.
  - Changed data URLs in manager since the `v1` API requires a different route to get
    to the data directories.
    ```python
    # Old URL.
    AUDIO_URL = "https://homes.esat.kuleuven.be/~btamm/fpack_webapp/v0/data/fpack/audio"
    # New URL.
    AUDIO_URL = "https://homes.esat.kuleuven.be/~btamm/fpack_webapp/v1/data/audio"
    ```
- Bumped version to v1.0.0
