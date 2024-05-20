#!/usr/bin/python3
"""
sends request to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = sys.argv[1]
        if len(query) <= 1 or not isinstance(query, chr):
            response = requests.post('http://0.0.0.0:5000/search_user', data={"q": ""})  # Changed to POST
        else:
            response = requests.post('http://0.0.0.0:5000/search_user', data={"q": query})  # Changed to POST
    else:
        response = requests.post('http://0.0.0.0:5000/search_user', data={"q": ""})  # Changed to POST

    # Check if the response status code indicates success
    if response.status_code == 200:
        data = response.json()
        if not data:
            print("No result")
        else:
            print(f"[{data['id']}] {data['name']}")
    else:
        print(f"Request failed with status code {response.status_code}")
