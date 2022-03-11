#!/bin/bash

# If "make" is not installed (e.g. Windows), then this will also work.

# Exit if any command fails.
set -e

# OS-dependent variables.
if [[ "$OSTYPE" == "msys" ]]; then
    # Windows.
    PYTHON_INTERPRETER="python"
    ACTIVATE_CMD="source venv/Scripts/activate"
else
    # Linux.
    PYTHON_INTERPRETER="python3"
    ACTIVATE_CMD="source venv/bin/activate"
fi


# Make order:
# test_environment -> activate_venv -> requirements -> app

# 1. test_environment
$PYTHON_INTERPRETER test_environment.py

# 2. activate_venv
$ACTIVATE_CMD

# 3. requirements
$PYTHON_INTERPRETER -m pip install -U pip setuptools wheel
$PYTHON_INTERPRETER -m pip install -r requirements.txt

# 4. app
$PYTHON_INTERPRETER src/app.py