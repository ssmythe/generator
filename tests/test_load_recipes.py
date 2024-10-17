def test_load_recipes():
    from app import load_blocks, load_recipes
    blocks_dir = "test_data/blocks/"
    recipes_dir = "test_data/recipes/"
    blocks = load_blocks(blocks_dir)
    recipes = load_recipes(recipes_dir, blocks)

    assert isinstance(recipes, dict)
    assert len(recipes) == 3
    assert recipes["abc"] == "a\nb\nc\n"
    assert recipes["greeting"] == "Hello, {{ name }}!\n"
    assert recipes["farewell"] == "Goodbye, {{ .name }}!\n"
