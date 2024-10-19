#!/usr/bin/env bats

setup() {
  rm -rf test_output_dir
  mkdir test_output_dir
}

teardown() {
  rm -rf test_output_dir
}

# Test the --output option
@test "--output option writes rendered recipes to directory" {
  run coverage run --append ./generator.py --list test_data/lists/simple-jinja2-gomplate --output test_output_dir
  echo "Command Output: $output"
  echo "Exit Status: $status"
  [ "$status" -eq 0 ]

  # Check if the expected output files are created in the directory
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

# Test the -o shorthand option
@test "-o option writes rendered recipes to directory" {
  run coverage run --append ./generator.py -l test_data/lists/simple-jinja2-gomplate -o test_output_dir
  echo "Command Output: $output"
  echo "Exit Status: $status"
  [ "$status" -eq 0 ]

  # Check if the expected output files are created in the directory
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

# Test the -o shorthand option
@test "-o option writes rendered recipes to directory" {
  run coverage run --append ./generator.py -l test_data/lists/simple-jinja2-gomplate -o test_output_dir
  echo "Command Output: $output"
  echo "Exit Status: $status"
  [ "$status" -eq 0 ]

  # Check if the expected output files are created in the directory
  [ -f "test_output_dir/simple.txt" ]
  [ -f "test_output_dir/greeting.txt" ]
  [ -f "test_output_dir/farewell.txt" ]
}
