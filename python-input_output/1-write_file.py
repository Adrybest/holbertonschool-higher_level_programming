#!/usr/bin/python3
"""Defines a text file-writing function"""


def write_file(filename="", text=""):
    """Returns the number of lines of a text file"""

    with open(filename, 'w', encoding="utf-8") as f:
        i = f.write(text)
    return i
