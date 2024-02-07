#!/usr/bin/python3
"""save json to file"""
import json


def save_to_json_file(my_obj, filename):
    """save json to file"""
    with open(filename, mode='w', encoding="utf-8") as f:
        return (json.dump(my_obj, f))
