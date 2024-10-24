#!/usr/bin/env bats

setup() {
  rm -rf test_output_dir
}

teardown() {
  rm -rf test_output_dir
}

# Test missing list file shows an error
@test "missing list file shows an error" {
  run coverage run --append ./generator.py --list non_existent_list --output test_output_dir
  [ "$status" -ne 0 ]
  [[ "$output" == *"Error: List file non_existent_list does not exist."* ]]
}

# Test missing output option shows usage
@test "missing output option shows usage" {
  run coverage run --append ./generator.py --list test_data/lists/sample_list
  [ "$status" -ne 0 ]
  [[ "$output" == *"usage:"* ]]
}
