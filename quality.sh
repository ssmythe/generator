#!/usr/bin/env bash

# Clean previous coverage data
echo "Cleaning previous coverage data..."
coverage erase

# Run pytest with coverage and generate an HTML report
echo "Running pytest with coverage..."
coverage run -m pytest

# Run BATS tests with coverage
echo "Running BATS tests with coverage..."
bats_tests_dir="tests/bats"
for test_file in "$bats_tests_dir"/*.bats; do
  echo "Running BATS test: $test_file"
  BATS_COVERAGE="coverage run --append" bats "$test_file"
done

# Combine the coverage from pytest and BATS
echo "Combining coverage data..."
coverage combine

# Generate the coverage report and HTML output
echo "Generating coverage report..."
coverage report
coverage html

echo "Quality checks completed. Open htmlcov/index.html to view the coverage report."
