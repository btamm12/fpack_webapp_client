# Changelog

This folder contains the changelogs of the project, grouped by MAJOR version (see
[semantic versioning](https://semver.org/spec/v2.0.0.html)).

## 1. What is a changelog?
A changelog is a file which contains a curated, chronologically ordered list of
notable changes for each version of a project.

## 2. Why keep a changelog?
To make it easier for users and contributors to see precisely what notable changes
have been made between each release (or version) of the project.

## 3. Who needs a changelog?
People do. Whether consumers or developers, the end users of software are human
beings who care about what's in the software. When the software changes, people want
to know why and how.

**Source:** https://keepachangelog.com/en/1.0.0/

## 4. Template Changelog
When creating a new file, use the following template. `[N]` represents the MAJOR
version number.

**Remove any sections (Added, Changed, Deprecated, Removed, Fixed, Security) that are
not used.**

*changelog_v[N].md*
```
# Changelog - Versions [N].x.x

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


## `v[N].0.0`

**Title:** Released XYZ \
**Release Date:** YYYY-MM-DD

### Added
- ...

### Changed
- ...

### Deprecated
- ...

### Removed
- ...

### Fixed
- ...

### Security
- ...

```

## 5. Template Planned Changes
When planning and implementing changes, use the file `planned_changes.md` to keep
track of everything. This will also make writing the changelog easy. `[N]` represents
the MAJOR version number.

*planned_changes.md*
```
# Planned Changes

## `v[N].x.x`

**Title:** Released XYZ \
**Release Date:** N/A

### Added
- **Finished:**
  - ...
- **Work In Progress:**
  - ...
- **To-Do:**
  -  ...

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
  -  ...

### Security
- **Finished:**
  - ...
- **Work In Progress:**
  - ...
- **To-Do:**
  -  ...

```
