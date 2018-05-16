#!/usr/bin/python3
def read_file(filename=""):
    """read in a file
    Args:
        filename: the file's name
    """
    with open(filename, 'r') as f:
        content = f.read()
    print(content)
    f.close()
