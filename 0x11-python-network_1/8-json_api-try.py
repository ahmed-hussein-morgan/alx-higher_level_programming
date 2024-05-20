#!/usr/bin/python3
"""
sends request to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) <= 1 or not isinstance(sys.argv[1], chr):
        response = requests.\
            get('http://0.0.0.0:5000/search_user', params={'q': ""})
    else:
        response = requests.\
            get('http://0.0.0.0:5000/search_user', params={'q': {sys.argv[1]}})
    if not response.json():
        print("Not a valid JSON")
    elif len(response.json()) == 0:
        print("No result")
    else:
        print(f"[{response.json([id])}] {response.json([__name__])}")
