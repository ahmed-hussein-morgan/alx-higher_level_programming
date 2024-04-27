#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request
import urllib.parse
import sys

# Check if a URL and an email are provided as command-line arguments
if len(sys.argv) < 3:
    print("Usage: python3 script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Prepare the POST data
data = urllib.parse.urlencode({'email': email})
data = data.encode('ascii') # Encode the data to bytes

# Send a POST request to the URL with the email as a parameter
with urllib.request.urlopen(url, data=data) as response:
    # Read the response body
    body = response.read()
    # Decode the response body from bytes to a UTF-8 string
    body_utf8 = body.decode('utf-8')
    # Print the response body
    print(body_utf8)
