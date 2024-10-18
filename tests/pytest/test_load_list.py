def test_load_list():
    from generator import load_list

    list_file = "test_data/lists/sample_list"

    # Expected format for each line in sample_list
    expected_data = [
        ("test_data/blocks/simple", "test_data/recipes/simple", "test_data/vars/empty.json"),
        ("test_data/blocks/jinja2", "test_data/recipes/jinja2", "test_data/vars/greeting.json"),
        ("test_data/blocks/gomplate", "test_data/recipes/gomplate", "test_data/vars/farewell.json")
    ]

    result = load_list(list_file)

    assert result == expected_data
