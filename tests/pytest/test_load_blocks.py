import os
import pytest
import tempfile
from generator import load_blocks


def test_load_blocks_simple():
    blocks_dir = "test_data/blocks/simple/"
    blocks = load_blocks(blocks_dir)

    assert isinstance(blocks, dict)
    assert len(blocks) == 3
    assert blocks["a"] == "a\n"
    assert blocks["b"] == "b\n"
    assert blocks["c"] == "c\n"


def test_load_blocks_jinja2():
    blocks_dir = "test_data/blocks/jinja2/"
    blocks = load_blocks(blocks_dir)

    assert isinstance(blocks, dict)
    assert len(blocks) == 1
    assert blocks["greeting"] == "Hello, {{ name }}!\n"


def test_load_blocks_gomplate():
    blocks_dir = "test_data/blocks/gomplate/"
    blocks = load_blocks(blocks_dir)

    assert isinstance(blocks, dict)
    assert len(blocks) == 1
    assert blocks["farewell"] == "Goodbye, {{ .name }}!\n"


def test_load_blocks_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Ensure the directory is empty
        assert len(os.listdir(temp_dir)) == 0
        blocks = load_blocks(temp_dir)

        # Check that the loaded blocks are an empty dictionary
        assert isinstance(blocks, dict)
        assert len(blocks) == 0


def test_load_blocks_missing_directory():
    # Test for a missing directory
    with pytest.raises(FileNotFoundError):
        load_blocks("non_existent_directory/")
