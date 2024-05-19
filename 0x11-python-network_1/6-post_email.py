#!/usr/bin/python3
"""POST request with the email, displays the body of the response"""
import sys
import requests

response = requests.post(sys.argv[1], sys.argv[2])
print(f"Your email is: {response.content}")
