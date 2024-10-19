from generator import load_vars
import pytest
import tempfile
import os


def test_load_vars():
    vars_file = "test_data/vars/greeting.json"

    # Load the variables from the JSON file
    vars_data = load_vars(vars_file)

    # Validate that the variables and delimiters are correctly loaded
    assert "delimiters" in vars_data
    assert "vars" in vars_data

    # Validate delimiters
    assert vars_data["delimiters"]["left_delimiter"] == "{{ "
    assert vars_data["delimiters"]["right_delimiter"] == " }}"

    # Validate variables
    assert vars_data["vars"]["name"] == "world"


def test_load_missing_vars_file():
    # Test for a missing directory
    with pytest.raises(FileNotFoundError):
        load_vars("non_existent_file")


def test_load_invalid_vars_file():
    # Create a temporary file with invalid JSON content
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
        temp_file.write("{ invalid json }")
        temp_filename = temp_file.name

    # Test for JSONDecodeError in load_vars
    with pytest.raises(SystemExit):
        load_vars(temp_filename)

    # Clean up the temporary file
    os.remove(temp_filename)
