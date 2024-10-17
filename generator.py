import os
import json


def load_blocks(directory):
    blocks = {}
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r') as file:
            blocks[filename] = file.read()
    return blocks


def load_recipes(directory, blocks):
    recipes = {}
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r') as file:
            content = file.read().splitlines()
            combined = "".join([blocks[line] for line in content])
            recipes[filename] = combined
    return recipes


def load_vars(vars_file):
    with open(vars_file, 'r') as file:
        vars_data = json.load(file)
    return vars_data


def apply_vars(content, vars_data):
    left_delim = vars_data["delimiters"]["left_delimiter"]
    right_delim = vars_data["delimiters"]["right_delimiter"]

    # Replace each variable in the content
    for var, value in vars_data["vars"].items():
        placeholder = f"{left_delim}{var}{right_delim}"
        content = content.replace(placeholder, value)

    return content
