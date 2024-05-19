#!/usr/bin/python3
"""catch the error"""

from urllib.request import urlopen
import sys
from urllib.error import HTTPError, URLError


if __name__ == "__main__":
    try:
        with urlopen(sys.argv[1]) as response:
            html = response.read().decode()

        print(html)

    except HTTPError as error:
        # print(f"Error code: {error.code} {error.reason}")
        print(f"Error code: {error.code}")
