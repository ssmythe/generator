#!/usr/bin/env python3

import argparse
import os
import json
import sys


def load_blocks(blocks_dir):
    blocks = {}
    if not os.path.exists(blocks_dir):
        raise FileNotFoundError(f"The directory '{blocks_dir}' does not exist.")

    for block_file in os.listdir(blocks_dir):
        block_path = os.path.join(blocks_dir, block_file)
        if os.path.isfile(block_path):
            with open(block_path, "r", encoding="utf-8") as f:
                content = f.read()
                blocks[os.path.splitext(block_file)[0]] = content

    return blocks


def load_recipes(directory, blocks):
    """Load and assemble recipes using the blocks."""
    recipes = {}
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        with open(file_path, "r") as file:
            # Step 1: Read recipe file as is
            recipe_content = file.read().splitlines()

            # Step 2: Concatenate blocks together
            combined_content = "".join(blocks.get(line, f"{{missing block: {line}}}") for line in recipe_content)

            # Step 3: Put concatenated content into recipe dictionary
            recipes[os.path.splitext(filename)[0]] = combined_content

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
    """Load the blocks directory, recipes directory, vars file, and output filename from each line in the list file."""
    try:
        with open(list_file, "r") as file:
            data = []
            for line in file:
                parts = line.strip().split(",")
                if len(parts) != 4:
                    raise ValueError(
                        f"Invalid line in list file: {line.strip()}. Expected format: 'blocks_dir,recipes_dir,vars_file,output_filename'."
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
        "delimiters", {"left_delimiter": "{{ ", "right_delimiter": " }}"}
    )
    for key, value in vars_data.get("vars", {}).items():
        recipe_content = recipe_content.replace(
            f'{delimiters["left_delimiter"]}{key}{delimiters["right_delimiter"]}',
            value,
        )
    return recipe_content


def assemble_recipe(recipe_name, recipes, vars_data):
    """Assemble the recipe using the provided recipe content and perform variable substitution."""
    # Get the recipe content from the recipes dictionary
    if recipe_name not in recipes:
        raise FileNotFoundError(f"Recipe '{recipe_name}' not found in recipes.")
    assembled_recipe = recipes[recipe_name]

    # Perform variable substitution if applicable
    delimiters = vars_data.get("delimiters", {})
    left_delim = delimiters.get("left_delimiter", "{{ ")
    right_delim = delimiters.get("right_delimiter", " }}")
    for key, value in vars_data.get("vars", {}).items():
        assembled_recipe = assembled_recipe.replace(f"{left_delim}{key}{right_delim}", value)
    
    return assembled_recipe


def process_list(list_file, output_dir):
    """Process the list file and output the generated files."""
    # Load the list file
    list_data = load_list(list_file)

    # Iterate through each list entry and process accordingly
    for blocks_dir, recipe_file, vars_file, output_file in list_data:
        # Load blocks, recipes, and vars
        blocks = load_blocks(blocks_dir)
        recipes_dir = os.path.dirname(recipe_file)
        recipe_name = os.path.basename(recipe_file)
        recipes = load_recipes(recipes_dir, blocks)
        vars_data = load_vars(vars_file)

        # Generate the output path
        output_path = os.path.join(output_dir, os.path.basename(output_file))

        # Assemble the recipe using the loaded components
        assembled_content = assemble_recipe(recipe_name, recipes, vars_data)

        # Write the assembled content to the output file
        with open(output_path, "w") as f:
            f.write(assembled_content)

    print(f"Processed list from {list_file} and saved output to {output_dir}")



def main():
    parser = argparse.ArgumentParser(description="CLI for Generator Script")
    parser.add_argument(
        "--list",
        "-l",
        type=str,
        help="Set the list file containing directories, vars info, and output filenames",
        required=True,
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        help="Set the top-level output directory for rendered files",
        required=True,
    )

    args = parser.parse_args()

    # Ensure output directory exists
    if not os.path.exists(args.output):
        os.makedirs(args.output)

    # Load list file data (blocks_dir, recipes_dir, vars_file, output_filename)
    list_entries = load_list(args.list)

    # Process each entry in the list file
    for blocks_dir, recipes_dir, vars_file, output_filename in list_entries:
        vars_data = load_vars(vars_file)

        # Process each recipe in the directory
        for recipe_filename in os.listdir(recipes_dir):
            recipe_file = os.path.join(recipes_dir, recipe_filename)
            recipe_content = assemble_recipe(recipe_file, blocks_dir)
            final_content = apply_vars(recipe_content, vars_data)

            # Apply vars substitution to the output filename
            final_output_filename = apply_vars(output_filename, vars_data)

            # Write the final content to the output file
            output_file_path = os.path.join(args.output, final_output_filename)
            with open(output_file_path, "w") as output_file:
                output_file.write(final_content)
                print(f"Rendered output written to: {output_file_path}")


if __name__ == "__main__":
    main()
