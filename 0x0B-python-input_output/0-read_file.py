#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r') as f:
        content = f.read()
    print(content)
    f.close()
