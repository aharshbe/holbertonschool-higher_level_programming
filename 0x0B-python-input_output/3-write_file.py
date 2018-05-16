#!/usr/bin/python3
def write_file(filename="", text=""):
    """write a string to a text file
    Args:
        filename: the file's name
        test: file to write to
    """
    with open(filename, 'w') as f:
        count = f.write(text)
    f.close()
    return count
