#!/usr/bin/env python3

import argparse
import os
import json
import sys


def load_blocks(directory):
    """Load all blocks from the specified directory."""
    blocks = {}
    try:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r") as file:
                blocks[filename] = file.read()
    except FileNotFoundError:
        print(f"Error: Directory {directory} does not exist.")
        sys.exit(1)
    return blocks


def load_recipes(directory, blocks):
    """Load and assemble recipes using the blocks."""
    recipes = {}
    try:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r") as file:
                recipe_content = file.read().splitlines()
                combined_content = "".join(
                    [
                        blocks.get(line, f"{{missing block: {line}}}")
                        for line in recipe_content
                    ]
                )
                recipes[filename] = combined_content
    except FileNotFoundError:
        print(f"Error: Directory {directory} does not exist.")
        sys.exit(1)
    return recipes


def load_vars(vars_file):
    """Load variables from a JSON vars file."""
    try:
        with open(vars_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Vars file {vars_file} does not exist.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in vars file {vars_file}.")
        sys.exit(1)


def load_list(list_file):
    """Load the blocks directory, recipes directory, and vars file from each line in the list file."""
    try:
        with open(list_file, "r") as file:
            data = []
            for line in file:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    raise ValueError(
                        f"Invalid line in list file: {line.strip()}. Expected format: 'blocks_dir,recipes_dir,vars_file'."
                    )
                data.append(tuple(parts))
        return data
    except FileNotFoundError:
        print(f"Error: List file {list_file} does not exist.")
        sys.exit(1)
    except ValueError as e:
        print(e)
        sys.exit(1)


def apply_vars(recipe_content, vars_data):
    """Apply variables to the recipe content."""
    delimiters = vars_data.get(
        "delimiters", {"left_delimiter": "{{", "right_delimiter": "}}"}
    )
    for key, value in vars_data.get("vars", {}).items():
        recipe_content = recipe_content.replace(
            f'{delimiters["left_delimiter"]}{key}{delimiters["right_delimiter"]}',
            value,
        )
    return recipe_content


def assemble_recipe(recipe_file, blocks_dir):
    """Assemble the recipe using blocks."""
    try:
        with open(recipe_file, "r") as file:
            block_names = file.read().splitlines()

        assembled_recipe = ""
        for block_name in block_names:
            block_file = os.path.join(blocks_dir, block_name)
            if os.path.exists(block_file):
                with open(block_file, "r") as block:
                    assembled_recipe += block.read() + "\n"
            else:
                print(f"Error: Block {block_name} not found.")
                sys.exit(1)  # Ensure we raise SystemExit here
        return assembled_recipe
    except FileNotFoundError:
        print(f"Error: Recipe file {recipe_file} does not exist.")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="CLI for Generator Script")
    parser.add_argument(
        "--list",
        "-l",
        type=str,
        help="Set the list file containing directories and vars info",
        required=True,
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        help="Set the output file for rendered recipes",
        required=True,
    )

    args = parser.parse_args()

    # Load list file data (blocks_dir, recipes_dir, vars_file)
    list_file = args.list
    if not os.path.exists(list_file):
        print(f"Error: List file {list_file} does not exist.")
        sys.exit(1)

    # Load all entries from the list file
    list_entries = load_list(list_file)

    # Open output file for writing
    with open(args.output, "w") as output_file:
        for blocks_dir, recipes_dir, vars_file in list_entries:
            vars_data = load_vars(vars_file)

            # Process each recipe in the directory
            for recipe_filename in os.listdir(recipes_dir):
                recipe_file = os.path.join(recipes_dir, recipe_filename)
                recipe_content = assemble_recipe(recipe_file, blocks_dir)
                final_content = apply_vars(recipe_content, vars_data)
                output_file.write(final_content + "\n")

    print(f"Rendered output written to: {args.output}")


if __name__ == "__main__":
    main()
