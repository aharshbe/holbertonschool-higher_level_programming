#!/usr/bin/python3
def read_file(filename=""):
    """read in a file
    Args:
        filename: the file's name
    """
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)
    return
