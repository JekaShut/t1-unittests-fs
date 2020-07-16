from file_1 import File

contents = ["Hello world!", 0, "_3H"]
filenames = ["filename", 0, "_3H"]



def test_get_size():
    n = 0
    for x in contents:
        test = File(filenames[n], contents[n]).get_size()
        assert test == len(contents[n])
        n = n + 1

def test_get_filename():
    n = 0
    for x in filenames:
        test = File(filenames[n], contents[n]).get_filename()
        assert test == filenames[n]
        
    

