
# Generator

## Overview

The Generator is a Python command-line tool that processes blocks of text, aggregates them into recipes, applies variable substitutions, and writes the final output to a file. The blocks, recipes, and variables are defined in a structured way, and the app allows you to specify multiple lists of directories and variables to generate multiple outputs.

## Features

- **Blocks**: Individual pieces of content that can be assembled into larger outputs.
- **Recipes**: Files that reference block names and combine them into structured outputs.
- **Variable Substitution**: Replaces placeholders in recipes with values from a JSON file.
- **List Files**: Manages block, recipe, and variable directories in a CSV format.
- **Error Handling**: Provides feedback for missing or incorrect files.

## Requirements

- Python 3.8 or newer
- Dependencies listed in `requirements.txt` (can be installed using `pip`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ssmythe/generator.git
   cd generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Make sure the script is executable:
   ```bash
   chmod +x generator.py
   ```

## Usage

```bash
./generator.py --list <list_file> --output <output_dir>
```

### Options:
- `--list`, `-l`: Path to the CSV file containing block, recipe, and vars directories.
- `--output`, `-o`: Output directory where the rendered recipe files will be saved.

### Example:

```bash
./generator.py --list test_data/lists/sample_list --output output_dir
```

The list file should have the following format:

```
<blocks_directory>,<recipes_directory>,<vars_file>,<output_filename>
```

Example `sample_list`:

```
test_data/blocks/simple,test_data/recipes/simple,test_data/vars/empty.json,simple.txt
test_data/blocks/jinja2,test_data/recipes/jinja2,test_data/vars/greeting.json,greeting.txt
test_data/blocks/gomplate,test_data/recipes/gomplate,test_data/vars/farewell.json,farewell.txt
```

This structure allows the generator to process multiple block directories, recipes, and variable files in one run and write the rendered content to files in the output directory.

### Blocks

A block is a text file located in a block directory. Blocks can be used in recipes by referring to their filenames.

Example `block1.txt`:

```
Hello, {{name}}!
```

### Recipes

A recipe contains a list of block filenames. The generator assembles the blocks in the order they are listed.

Example `greeting.recipe`:

```
block1.txt
block2.txt
```

### Vars

Vars files are JSON files that map variable names to their values. These values are substituted in the final output.

Example `vars.json`:

```json
{
  "delimiters": {
    "left_delimiter": "{{",
    "right_delimiter": "}}"
  },
  "vars": {
    "name": "Alice",
    "farewell": "Goodbye"
  }
}
```

### Full Command Example

```bash
./generator.py --list test_data/lists/sample_list --output output_dir
```

This command will:
1. Load the blocks and recipes as defined in `sample_list`.
2. Perform variable substitutions using the vars files.
3. Write the final assembled outputs to files in the specified output directory.

## Testing

The project uses both `pytest` and `BATS` for testing.

### Run All Tests

```bash
./quality.sh
```

This script will:
1. Run `pytest` for unit tests with coverage.
2. Run `BATS` for command-line interface testing.
3. Combine the coverage results into a single report.

The final coverage report will be available in `htmlcov/index.html`.
