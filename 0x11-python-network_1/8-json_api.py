#!/usr/bin/python3
"""
sends request to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = sys.argv[1]
        if len(query) <= 1 or not isinstance(query, str):
            response =\
                requests.get('http://0.0.0.0:5000/search_user', params={'q': ""})
        else:
            response =\
                requests.get('http://0.0.0.0:5000/search_user', params={'q': query})
    else:
        response = \
            requests.get('http://0.0.0.0:5000/search_user', params={'q': ""})

    if not response.json():
        print("Not a valid JSON")
    elif len(response.json()) == 0:
        print("No result")
    else:
        print(f"[{response.json()['id']}] {response.json()['name']}")
