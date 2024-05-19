#!/usr/bin/python3
"""POST request with the email, displays the body of the response"""
import sys
import requests

if __name__ == "__main__":
    response = requests.post(sys.argv[1], data={'email': {sys.argv[2]}})
    decoded_content = response.content.decode()
    print(decoded_content)
