#!/usr/bin/env bats

setup() {
  rm -rf test_output_dir
  mkdir test_output_dir
}

teardown() {
  rm -rf test_output_dir
}

# Test the --list or -l option processes the list file
@test "--list option processes the list file" {
  run coverage run --append ./generator.py --list test_data/lists/sample_list --output test_output_dir
  [ "$status" -eq 0 ]

  # Check that the expected output files are created in the output directory
  [ -f "test_output_dir/simple.txt" ]
  [ -f "test_output_dir/greeting.txt" ]
  [ -f "test_output_dir/farewell.txt" ]
}

@test "-l option processes the list file" {
  run coverage run --append ./generator.py -l test_data/lists/sample_list --output test_output_dir
  [ "$status" -eq 0 ]

  # Check that the expected output files are created in the output directory
  [ -f "test_output_dir/simple.txt" ]
  [ -f "test_output_dir/greeting.txt" ]
  [ -f "test_output_dir/farewell.txt" ]
}
