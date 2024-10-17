#!/usr/bin/env bash

# Set the PYTHONPATH to the current directory (root directory)
export PYTHONPATH=$(pwd)

# Run pytest with coverage and generate an HTML report
pytest --cov=. --cov-report=html
