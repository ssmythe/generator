#!/usr/bin/env bats

setup() {
  rm -rf test_output_dir
  mkdir -p test_output_dir
}

teardown() {
  rm -rf test_output_dir
}

@test "--list option processes the simple list file" {
  run coverage run --append ./generator.py --list test_data/lists/simple --output test_output_dir
  # echo "Output: $output"
  # echo "Status: $status"
  [ "$status" -eq 0 ]

  # Check that the expected output files are created in the output directory
  [ -f "test_output_dir/simple.txt" ]

  # Validate content of output files
  run cat test_output_dir/simple.txt
  # Split the output by newline and check each line individually
  lines=($(echo "$output"))
  [ "${lines[0]}" = "a" ]
  [ "${lines[1]}" = "b" ]
  [ "${lines[2]}" = "c" ]
}

@test "--list option processes the simple-jinja2-gomplate list file" {
  run coverage run --append ./generator.py --list test_data/lists/simple-jinja2-gomplate --output test_output_dir
  echo "Output: $output"
  echo "Status: $status"
  [ "$status" -eq 0 ]

  # Check that the expected output files are created in the output directory
  [ -f "test_output_dir/simple.txt" ]
  [ -f "test_output_dir/greeting.txt" ]
  [ -f "test_output_dir/farewell.txt" ]

  # Validate content of output files
  run cat test_output_dir/simple.txt
  lines=($(echo "$output"))
  [ "${lines[0]}" = "a" ]
  [ "${lines[1]}" = "b" ]
  [ "${lines[2]}" = "c" ]

  run cat test_output_dir/greeting.txt
  [ "$output" = "Hello, world!" ]

  run cat test_output_dir/farewell.txt
  [ "$output" = "Goodbye, world!" ]
}
