import tempfile
from generator import load_list  # Import the function you're testing


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
