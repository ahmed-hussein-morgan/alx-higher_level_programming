#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request
import sys
if len(sys.argv) < 2:
    print("Usage: python3 script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

# Send a request to the URL
with urllib.request.urlopen(url) as response:
    # Get the headers from the response
    headers = response.headers
    # Find the X-Request-Id header
    x_request_id = headers.get('X-Request-Id')
    # Print the X-Request-Id value
    print(x_request_id)
