#!/usr/bin/python3
"""start using request package"""
import requests

response = requests.get("https://alx-intranet.hbtn.io/status")
decode_content = response.content.decode('utf-8')
# print(dir(requests.get))
print(f"Body response:\n\t- type: {type(decode_content)}\n\
\t- content: {decode_content}")
