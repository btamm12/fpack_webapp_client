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
# clean -> test_environment -> activate_venv -> requirements -> app

# 1. clean
find . -type f -name "*.py[co]" -delete
find . -type d -name "__pycache__" -delete

# 2. test_environment
$PYTHON_INTERPRETER test_environment.py

# 3. activate_venv
$ACTIVATE_CMD

# 4. requirements
$PYTHON_INTERPRETER -m pip install -U pip setuptools wheel
$PYTHON_INTERPRETER -m pip install -r requirements.txt

# 5. migration
$PYTHON_INTERPRETER src/app.py