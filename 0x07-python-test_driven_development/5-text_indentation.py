#!/usr/bin/python3
"""
    Prints a text with 2 new lines after
    special character

"""


def text_indentation(text):
    """
        Replace special character with 2 new lines
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for ch in [':', '.', '?']:
        if ch in text:
            text = text.replace(ch, ch+'\n')
    s = [s.strip() for s in text.split('\n')]
    print("\n\n".join(s), end='')
