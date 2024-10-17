def test_load_vars():
    from app import load_vars
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
