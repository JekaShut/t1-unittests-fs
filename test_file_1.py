from file_1 import File

content = "Hello world!"
filename = "filename"


def test_get_size():
    test = File(filename, content).get_size()
    assert test == len(content)

def test_get_filename():
    test = File(filename, content).get_filename()
    assert test == filename
    assert test == filename

