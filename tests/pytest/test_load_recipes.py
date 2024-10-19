from generator import load_blocks, load_recipes
import pytest


def test_load_recipes_simple():
    blocks_dir = "test_data/blocks/simple/"
    recipes_dir = "test_data/recipes/simple/"
    blocks = load_blocks(blocks_dir)
    recipes = load_recipes(recipes_dir, blocks)

    assert isinstance(recipes, dict)
    assert len(recipes) == 1
    assert recipes["abc"] == "a\nb\nc\n"


def test_load_recipes_jinja2():
    blocks_dir = "test_data/blocks/jinja2/"
    recipes_dir = "test_data/recipes/jinja2/"
    blocks = load_blocks(blocks_dir)
    recipes = load_recipes(recipes_dir, blocks)

    assert isinstance(recipes, dict)
    assert len(recipes) == 1
    assert recipes["greeting"] == "Hello, {{ name }}!\n"


def test_load_recipes_gomplate():
    blocks_dir = "test_data/blocks/gomplate/"
    recipes_dir = "test_data/recipes/gomplate/"
    blocks = load_blocks(blocks_dir)
    recipes = load_recipes(recipes_dir, blocks)

    assert isinstance(recipes, dict)
    assert len(recipes) == 1
    assert recipes["farewell"] == "Goodbye, {{ .name }}!\n"


def test_load_recipe_missing_directory():
    blocks_dir = "test_data/blocks/gomplate/"
    blocks = load_blocks(blocks_dir)
    # Test for a missing directory
    with pytest.raises(FileNotFoundError):
        load_recipes("non_existent_directory", blocks)
