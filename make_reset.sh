#!/bin/bash

# If "make" is not installed (e.g. Windows), then this will also work.

# Exit if any command fails.
set -e

# Make order:
# reset

# 1. reset
rm ./src/state.pkl
