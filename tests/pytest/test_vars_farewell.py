def test_vars_farewell():
    from generator import load_blocks, load_recipes, load_vars, apply_vars

    blocks_dir = "test_data/blocks/gomplate/"
    recipes_dir = "test_data/recipes/gomplate/"
    vars_file = "test_data/vars/farewell.json"

    # Load the blocks and recipes
    blocks = load_blocks(blocks_dir)
    recipes = load_recipes(recipes_dir, blocks)

    # Load the variables from the JSON file
    vars_data = load_vars(vars_file)

    # Apply the variables to the recipe (key should be 'farewell')
    final_output = apply_vars(recipes["farewell"], vars_data)

    # Assert the final output is as expected
    assert final_output == "Goodbye, world!\n"
