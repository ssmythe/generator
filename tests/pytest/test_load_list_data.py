import os
from generator import load_blocks, load_recipes, load_vars, load_list


def test_load_list_data():
    # Load the list file using the load_list function
    list_file = "test_data/lists/simple"
    list_data = load_list(list_file)

    # Extract the first line of list data
    blocks_dir, recipe_file, vars_file, output_file = list_data[0]

    # Validate blocks loading
    blocks = load_blocks(blocks_dir)
    assert isinstance(blocks, dict)
    assert len(blocks) == 3
    assert blocks["a"] == "a\n"
    assert blocks["b"] == "b\n"
    assert blocks["c"] == "c\n"

    # Validate recipe loading
    recipes_dir = os.path.dirname(recipe_file)
    recipe_name = os.path.basename(recipe_file)
    recipes = load_recipes(recipes_dir, blocks)
    assert isinstance(recipes, dict)
    assert len(recipes) == 1
    assert recipe_name in recipes
    assert recipes[recipe_name] == "a\nb\nc\n"

    # Validate vars loading
    vars_data = load_vars(vars_file)
    assert "delimiters" in vars_data
    assert "vars" in vars_data
    assert vars_data["delimiters"]["left_delimiter"] == "{{ "
    assert vars_data["delimiters"]["right_delimiter"] == " }}"
    assert vars_data["vars"] == {}

    # Validate output path extraction
    assert output_file == "tmp_output_dir/simple.txt"
