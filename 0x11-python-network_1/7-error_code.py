#!/usr/bin/python3
"""display error code"""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    decoded_response = response.content.decode()

    if response.status_code < 400:
        print(decoded_response)
    else:
        print(f"Error code: {response.status_code}")
