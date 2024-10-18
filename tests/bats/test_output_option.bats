#!/usr/bin/env bats

# Test the --output option
@test "--output option writes rendered recipes to file" {
  output_file="test_output.txt"
  run ./generator.py --list test_data/lists/sample_list --output $output_file
  echo "Command Output: $output"
  echo "Exit Status: $status"
  [ "$status" -eq 0 ]
  [ -f "$output_file" ]
}

# Test the -o shorthand option
@test "-o option writes rendered recipes to file" {
  output_file="test_output.txt"
  run ./generator.py -l test_data/lists/sample_list -o $output_file
  echo "Command Output: $output"
  echo "Exit Status: $status"
  [ "$status" -eq 0 ]
  [ -f "$output_file" ]
}
