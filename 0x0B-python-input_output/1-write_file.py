#!/usr/bin/python3
"""write to file"""


def write_file(filename="", text=""):
    """write to file"""
    with open(filename, mode='w', encoding="utf-8") as f:
        return (f.write(text))
