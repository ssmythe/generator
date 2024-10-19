def test_output_filename_variable_substitution():
    from generator import apply_vars

    # Define vars data with explicit delimiters
    vars_data = {
        "delimiters": {"left_delimiter": "{{", "right_delimiter": "}}"},
        "vars": {"username": "johndoe"},
    }

    # Filename template with variable to substitute
    output_filename_template = "output_{{username}}.txt"

    # Apply variable substitution
    final_output_filename = apply_vars(output_filename_template, vars_data)

    # Assert the final output filename is as expected
    assert final_output_filename == "output_johndoe.txt"
