def test_load_recipes_simple():
    from generator import load_blocks, load_recipes
    blocks_dir = "test_data/blocks/simple/"
    recipes_dir = "test_data/recipes/simple/"
    blocks = load_blocks(blocks_dir)
    recipes = load_recipes(recipes_dir, blocks)

    assert isinstance(recipes, dict)
    assert len(recipes) == 1
    assert recipes["abc"] == "a\nb\nc\n"


def test_load_recipes_jinja2():
    from generator import load_blocks, load_recipes
    blocks_dir = "test_data/blocks/jinja2/"
    recipes_dir = "test_data/recipes/jinja2/"
    blocks = load_blocks(blocks_dir)
    recipes = load_recipes(recipes_dir, blocks)

    assert isinstance(recipes, dict)
    assert len(recipes) == 1
    assert recipes["greeting"] == "Hello, {{ name }}!\n"


def test_load_recipes_gomplate():
    from generator import load_blocks, load_recipes
    blocks_dir = "test_data/blocks/gomplate/"
    recipes_dir = "test_data/recipes/gomplate/"
    blocks = load_blocks(blocks_dir)
    recipes = load_recipes(recipes_dir, blocks)

    assert isinstance(recipes, dict)
    assert len(recipes) == 1
    assert recipes["farewell"] == "Goodbye, {{ .name }}!\n"
