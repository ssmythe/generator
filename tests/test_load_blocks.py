# Test file: test_file_loader.py


def test_load_blocks():
    from generator import load_blocks
    blocks_dir = "test_data/blocks/"
    blocks = load_blocks(blocks_dir)

    assert isinstance(blocks, dict)
    assert len(blocks) == 5
    assert blocks["a"] == "a\n"
    assert blocks["b"] == "b\n"
    assert blocks["c"] == "c\n"
    assert blocks["farewell"] == "Goodbye, {{ .name }}!\n"
    assert blocks["greeting"] == "Hello, {{ name }}!\n"
    