#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """read in a file, print lines
    Args:
        filename: the file's name
    """
    with open(filename, 'r') as f:
        if not nb_lines:
            content = f.read()
            print(content)
            f.close()
            return
        for i in range(nb_lines):
            content = f.readline()
            print(content, end='')
            f.close()
            return (nb_lines)
