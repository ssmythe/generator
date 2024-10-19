import os
import tempfile
from generator import load_list, process_list


def test_process_list_simple():
    # Load the list file
    list_file = "test_data/lists/simple"

    # Create a temporary directory for output
    with tempfile.TemporaryDirectory() as temp_output_dir:
        # Process the list file using the process_list function
        process_list(list_file, temp_output_dir)

        # Validate the output file content
        output_file = os.path.join(temp_output_dir, "simple.txt")
        with open(output_file, "r") as f:
            result = f.read()

        expected_content = "a\nb\nc\n"
        assert result == expected_content


def test_process_list_combined():
    # Load the combined list file
    list_file = "test_data/lists/simple-jinja2-gomplate"

    # Create a temporary directory for output
    with tempfile.TemporaryDirectory() as temp_output_dir:
        # Process the list file using the process_list function
        process_list(list_file, temp_output_dir)

        # Validate the output file content for each recipe
        expected_results = {
            "simple.txt": "a\nb\nc\n",
            "greeting.txt": "Hello, world!\n",
            "farewell.txt": "Goodbye, world!\n",
        }

        for output_filename, expected_content in expected_results.items():
            output_file = os.path.join(temp_output_dir, output_filename)
            with open(output_file, "r") as f:
                result = f.read()
            assert result == expected_content
