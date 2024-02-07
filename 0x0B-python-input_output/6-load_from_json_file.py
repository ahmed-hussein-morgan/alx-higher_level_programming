#!/usr/bin/python3
"""save json from file"""
import json


def load_from_json_file(filename):
    """save json from file"""
    with open(filename, mode='r', encoding="utf-8") as f:
        loaded_file = json.load(f)
        return (loaded_file)
