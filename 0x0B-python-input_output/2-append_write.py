#!/usr/bin/python3
"""write at the end"""


def append_write(filename="", text=""):
    """write at the end"""
    with open(filename, mode='a', encoding="utf-8") as f:
        return (f.write(text))
