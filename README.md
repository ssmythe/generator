# Project: Generator

## Overview
This project is a Python-based content generator that assembles blocks of text into recipes, allowing for variable substitution. It is designed for command-line use and supports processing blocks, recipes, variables, and lists in a streamlined manner.

### Features:
- Load and concatenate text blocks.
- Assemble recipes from defined blocks.
- Substitute variables in the assembled content.
- Supports processing list files that specify blocks, recipes, vars, and output filenames.
- Command-line usage with options for list and output directories.

## Requirements
- Python 3.x
- Required Python libraries are specified in `requirements.txt`. Install them with:
  ```sh
  pip install -r requirements.txt
  ```
- Coverage (for running coverage tests)

## Installation
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd generator
   ```
2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
This project is designed to be run from the command line to generate content from blocks, recipes, and variables defined in separate files. The command-line options allow the user to specify a list file and output directory.

### Command-Line Options
- `--list` or `-l`: Specify the path to the list file.
- `--output` or `-o`: Specify the directory to save the output files.
- `--help`: Display usage instructions.

Example usage:
```sh
python generator.py --list test_data/lists/simple-jinja2-gomplate --output output_dir
```

## File Structure
- **blocks/**: Contains individual blocks of text that are loaded and concatenated.
- **recipes/**: Define the order in which blocks are concatenated.
- **vars/**: JSON files that contain variable definitions for substitution in the recipes.
- **lists/**: CSV files that list the blocks directory, recipe file, vars file, and output filename.
- **generator.py**: The main script to run the content generation process.
- **tests/**: Contains both pytest and BATS tests for different components.
  - `tests/pytest/`: Pytest files for unit testing the generator functions.
  - `tests/bats/`: BATS files for testing command-line options and overall integration.

## Testing
### Pytest
To run unit tests using pytest:
```sh
pytest -v tests/pytest/
```
### BATS
To run integration tests using BATS:
```sh
bats tests/bats/
```

## Example List File
An example list file (`simple-jinja2-gomplate`) contains lines specifying the blocks, recipe, vars, and output file. The format is:
```
<blocks_dir>,<recipe_file>,<vars_file>,<output_filename>
```
Example:
```
test_data/blocks/simple,test_data/recipes/simple/abc,test_data/vars/empty.json,tmp_output_dir/simple.txt
test_data/blocks/jinja2,test_data/recipes/jinja2/greeting,test_data/vars/greeting.json,tmp_output_dir/greeting.txt
test_data/blocks/gomplate,test_data/recipes/gomplate/farewell,test_data/vars/farewell.json,tmp_output_dir/farewell.txt
```

## Tests Overview
- **test_load_blocks.py**: Tests for loading blocks from the blocks directory.
- **test_load_recipes.py**: Tests for loading recipes from recipe files, including the `FileNotFoundError` condition.
- **test_load_vars.py**: Tests for loading variables from a JSON file, including a test for invalid JSON.
- **test_process_list.py**: Tests the process of reading from a list file and generating the corresponding output files.
- **test_output_options.bats**: Tests the command-line options for specifying the list file and output directory.
- **test_required_options.bats**: Tests the requirement of all necessary command-line options.
