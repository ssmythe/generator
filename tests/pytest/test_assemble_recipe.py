import pytest
from generator import assemble_recipe


def test_assemble_recipe():
    # Test data
    recipes = {"greeting": "Hello, {{ name }}!\n", "farewell": "Goodbye, {{ name }}!\n"}
    vars_data = {
        "delimiters": {"left_delimiter": "{{ ", "right_delimiter": " }}"},
        "vars": {"name": "world"},
    }

    # Test assembling the greeting recipe
    assembled_greeting = assemble_recipe("greeting", recipes, vars_data)
    assert assembled_greeting == "Hello, world!\n"

    # Test assembling the farewell recipe
    assembled_farewell = assemble_recipe("farewell", recipes, vars_data)
    assert assembled_farewell == "Goodbye, world!\n"

    # Test missing recipe
    with pytest.raises(
        FileNotFoundError, match="Recipe 'unknown' not found in recipes."
    ):
        assemble_recipe("unknown", recipes, vars_data)


if __name__ == "__main__":
    pytest.main()
