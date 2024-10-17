# Generator Project

This project is a Python-based generator that reads blocks of content, processes recipes, and applies token replacement using variables defined in JSON files. The project is set up with a test-driven development (TDD) approach and includes unit tests using `pytest` with coverage reports. BATS tests for command-line testing will be added soon.

## Features

- **Block Aggregation**: Reads blocks of content from files and assembles them into recipes.
- **Token Replacement**: Applies variable substitution in blocks using customizable delimiters.
- **Test-Driven Development (TDD)**: Tests are written using `pytest` to ensure the functionality is correct and well-tested.
- **Coverage Reports**: Generates HTML coverage reports using `pytest-cov`.
- **Command-Line Testing**: Plans to include BATS tests for command-line functionality.

## Project Structure

```plaintext
.
├── generator.py              # Main Python script for block loading, recipe processing, and token replacement
├── tests/
│   ├── pytest/               # Python unit tests using pytest
│   └── bats/                 # Placeholder for upcoming BATS command-line tests
├── test_data/                # Test data used for testing the generator functionality
├── cleanup.sh                # Remove unwanted generated files from python compilation and testing
├── quality.sh                # Script for running tests with coverage reports
└── README.md                 # This file
