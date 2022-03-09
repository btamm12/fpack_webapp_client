.PHONY: app clear_data create_environment requirements test_environment

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME = fpack_webapp_client
UNAME := $(shell uname)
ifeq ($(UNAME), Linux)
PYTHON_INTERPRETER = python3
ACTIVATE_CMD = "source venv/bin/activate"
endif
ifeq ($(UNAME), Windows)
PYTHON_INTERPRETER = python
ACTIVATE_CMD = "source venv/Scripts/activate"
endif




#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install Python Dependencies
requirements: test_environment
	$(PYTHON_INTERPRETER) -m pip install -U pip setuptools wheel
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt

## Create app
app: requirements
	$(PYTHON_INTERPRETER) src/app.py

## Migrate from old project
migration: requirements
	$(PYTHON_INTERPRETER) src/migration.py

## Reset app
#	find . -type f -name "*.py[co]" -delete
#	find . -type d -name "__pycache__" -delete
#	find ./data -type f -name "*.wav" -delete
#	find ./data -type f -name "*.TextGrid" -delete
#	find ./data -type f -name "*.html" -delete
reset:
	rm ./src/state.pkl


## Set up python interpreter environment
create_environment:
	$(PYTHON_INTERPRETER) -m pip install virtualenv
	$(PYTHON_INTERPRETER) -m virtualenv venv
	@echo ">>> Virtual environment created under venv/."
	@echo ">>> Activate using: $(ACTIVATE_CMD)"

## Test python environment is setup correctly
test_environment:
	$(PYTHON_INTERPRETER) test_environment.py
