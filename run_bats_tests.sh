#!/usr/bin/env bash

# Run all BATS tests located in tests/bats/
echo "Running BATS tests..."

# Check if BATS is installed
if ! command -v bats &>/dev/null; then
    echo "BATS is not installed. Please install BATS to run the tests."
    exit 1
fi

# Run the BATS tests
bats tests/bats/

# Capture the exit status of bats
status=$?

if [ $status -eq 0 ]; then
    echo "All BATS tests passed successfully."
else
    echo "Some BATS tests failed."
fi

# Exit with the status of the BATS run
exit $status
