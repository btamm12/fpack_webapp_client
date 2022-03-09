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


# Create virtual environment.
$PYTHON_INTERPRETER -m pip install virtualenv
$PYTHON_INTERPRETER -m virtualenv venv
echo ">>> Virtual environment created under venv/."
echo ">>> Activate using: $(ACTIVATE_CMD)"