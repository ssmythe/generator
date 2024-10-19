#!/usr/bin/env bats

setup() {
  rm -rf test_output_dir
  mkdir test_output_dir
}

teardown() {
  rm -rf test_output_dir
}

# Test that all required options are provided
@test "all required options are provided" {
  run coverage run --append ./generator.py --list test_data/lists/simple-jinja2-gomplate --output test_output_dir
  [ "$status" -eq 0 ]

  # Check if the expected output files are created in the directory
  [ -f "test_output_dir/simple.txt" ]
  [ -f "test_output_dir/greeting.txt" ]
  [ -f "test_output_dir/farewell.txt" ]
}

# Test missing options shows usage
@test "missing options shows usage" {
  run coverage run --append ./generator.py --list test_data/lists/simple-jinja2-gomplate
  echo "Command Output: $output"
  echo "Exit Status: $status"
  [[ "${output}" == *"usage:"* ]]
}

# Test help option displays usage
@test "help option displays usage" {
  run coverage run --append ./generator.py --help
  echo "Command Output: $output"
  echo "Exit Status: $status"
  [ "$status" -eq 0 ]
  [[ "${output}" == *"usage:"* ]]
}
