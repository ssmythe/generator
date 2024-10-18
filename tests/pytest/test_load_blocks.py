# Test file: test_file_loader.py


def test_load_blocks_simple():
    from generator import load_blocks
    blocks_dir = "test_data/blocks/simple/"
    blocks = load_blocks(blocks_dir)

    assert isinstance(blocks, dict)
    assert len(blocks) == 3
    assert blocks["a"] == "a\n"
    assert blocks["b"] == "b\n"
    assert blocks["c"] == "c\n"


def test_load_blocks_jinja2():
    from generator import load_blocks
    blocks_dir = "test_data/blocks/jinja2/"
    blocks = load_blocks(blocks_dir)

    assert isinstance(blocks, dict)
    assert len(blocks) == 1
    assert blocks["greeting"] == "Hello, {{ name }}!\n"


def test_load_blocks_gomplate():
    from generator import load_blocks
    blocks_dir = "test_data/blocks/gomplate/"
    blocks = load_blocks(blocks_dir)

    assert isinstance(blocks, dict)
    assert len(blocks) == 1
    assert blocks["farewell"] == "Goodbye, {{ .name }}!\n"
