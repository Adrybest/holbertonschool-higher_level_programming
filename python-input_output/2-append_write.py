#!/usr/bin/python3
"""Defines a text file-writing function"""


def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as f:
        w = f.write(text)
    return w