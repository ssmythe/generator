#!/usr/bin/env bats

# Test that all required options are provided
@test "all required options are provided" {
  output_file="test_output.txt"
  run coverage run --append ./generator.py --list test_data/lists/sample_list --output $output_file
  [ "$status" -eq 0 ]
  [ -f "$output_file" ]
}

# Test missing options shows usage
@test "missing options shows usage" {
  run coverage run --append ./generator.py --list test_data/lists/sample_list
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
