import tempfile
from generator import load_list  # Import the function you're testing
import pytest
import os


def test_load_list():
    list_file_content = """test_data/blocks/simple,test_data/recipes/simple,test_data/vars/abc.json,output_{{username}}.txt"""

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(list_file_content.encode("utf-8"))
        temp_file.close()
        list_data = load_list(temp_file.name)
        assert list_data == [
            (
                "test_data/blocks/simple",
                "test_data/recipes/simple",
                "test_data/vars/abc.json",
                "output_{{username}}.txt",
            )
        ]


def test_load_list_invalid_format():
    # Create a temporary file with an invalid line format
    with tempfile.NamedTemporaryFile(delete=False, mode="w") as temp_file:
        temp_file.write(
            "blocks_dir,recipes_dir,vars_file\n"
        )  # Missing the output_filename part
        temp_filename = temp_file.name

    # Test for ValueError in load_list
    with pytest.raises(SystemExit):
        load_list(temp_filename)

    # Clean up the temporary file
    os.remove(temp_filename)
