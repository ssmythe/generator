import pytest


def test_assemble_recipe_missing_block(tmpdir):
    from generator import assemble_recipe

    # Create a temporary blocks directory and a recipe file
    blocks_dir = tmpdir.mkdir("blocks")
    recipe_file = tmpdir.join("recipe.txt")
    recipe_file.write("missing_block")

    with pytest.raises(SystemExit):
        assemble_recipe(str(recipe_file), str(blocks_dir))


def test_assemble_recipe_missing_recipe_file():
    from generator import assemble_recipe

    # Set up a missing recipe file path
    recipe_file = "test_data/recipes/non_existent_recipe.txt"
    blocks_dir = "test_data/blocks/simple"

    with pytest.raises(SystemExit):
        assemble_recipe(recipe_file, blocks_dir)
