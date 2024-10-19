#!/usr/bin/env bats

setup() {
  rm -rf test_output_dir
  mkdir test_output_dir
}

teardown() {
  rm -rf test_output_dir
}

@test "Output file with variable substitution is created in correct directory" {
  run coverage run --append ./generator.py --list test_data/lists/sample_list --output test_output_dir

  # Check that the expected output files are created
  [ -f "test_output_dir/simple.txt" ]
  [ -f "test_output_dir/greeting.txt" ]
  [ -f "test_output_dir/farewell.txt" ]

  # Verify the content of simple.txt
  run cat "test_output_dir/simple.txt"
  [ "$status" -eq 0 ]
  [ "$output" = $'a\nb\nc' ]

  # Verify the content of greeting.txt (update this with the expected output)
  run cat "test_output_dir/greeting.txt"
  [ "$status" -eq 0 ]
  [ "$output" = "Hello, world!" ]

  # Verify the content of farewell.txt (update this with the expected output)
  run cat "test_output_dir/farewell.txt"
  [ "$status" -eq 0 ]
  [ "$output" = "Goodbye, world!" ]
}
