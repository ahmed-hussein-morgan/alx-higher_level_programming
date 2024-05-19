#!/usr/bin/python3
"""displays the value of the variable X-Request-Id"""

import requests
import sys

response = requests.get(sys.argv[1]).headers
print(response.get('X-Request-Id'))
