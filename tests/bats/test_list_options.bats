#!/usr/bin/env bats

# Test the --list or -l option processes the list file
@test "--list option processes the list file" {
  output_file="test_output.txt"
  run coverage run --append ./generator.py --list test_data/lists/sample_list --output $output_file
  [ "$status" -eq 0 ]
  [ -f "$output_file" ]
}

@test "-l option processes the list file" {
  output_file="test_output.txt"
  run coverage run --append ./generator.py -l test_data/lists/sample_list --output $output_file
  [ "$status" -eq 0 ]
  [ -f "$output_file" ]
}
