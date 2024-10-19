import pytest
import tempfile
from generator import load_list  # Import the function you're testing


def test_missing_list_file():
    from generator import load_list

    missing_list_file = "test_data/lists/non_existent_list"

    with pytest.raises(SystemExit):
        load_list(missing_list_file)


def test_malformed_list_file():
    malformed_content = "test_data/blocks/simple,test_data/recipes/simple"

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(malformed_content.encode("utf-8"))
        temp_file.close()

    with pytest.raises(SystemExit):
        load_list(temp_file.name)


def test_missing_blocks_dir():
    from generator import load_blocks

    missing_blocks_dir = "test_data/blocks/non_existent_blocks"

    with pytest.raises(SystemExit):
        load_blocks(missing_blocks_dir)


def test_missing_recipes_dir():
    from generator import load_recipes, load_blocks

    missing_recipes_dir = "test_data/recipes/non_existent_recipes"
    blocks_dir = "test_data/blocks/simple/"
    blocks = load_blocks(blocks_dir)

    with pytest.raises(SystemExit):
        load_recipes(missing_recipes_dir, blocks)


def test_missing_vars_file():
    from generator import load_vars

    missing_vars_file = "test_data/vars/non_existent_vars.json"

    with pytest.raises(SystemExit):
        load_vars(missing_vars_file)


def test_invalid_vars_json(tmpdir):
    from generator import load_vars

    invalid_vars_file = tmpdir.join("invalid_vars.json")
    invalid_vars_file.write("{ invalid json content }")

    with pytest.raises(SystemExit):
        load_vars(str(invalid_vars_file))
