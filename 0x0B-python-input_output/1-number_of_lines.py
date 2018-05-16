#!/usr/bin/python3
def number_of_lines(filename=""):
    """read in a file and cout lines
    Args:
        filename: the file's name
    """
    c = 0
    with open(filename, 'r') as f:
        for line in f:
            for i in line:
                if i == '\n':
                    c += 1
    f.close()
    return (c)
