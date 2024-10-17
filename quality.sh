#!/bin/bash

# Run pytest with coverage and generate an HTML report
pytest --cov=. --cov-report=html

# Check if pytest ran successfully
if [ $? -eq 0 ]; then
    echo "Pytest ran successfully with coverage report generated."
    echo "Open 'htmlcov/index.html' to view the coverage report."
else
    echo "Pytest encountered some issues."
    exit 1
fi
