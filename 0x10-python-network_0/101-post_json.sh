#!/bin/bash
# sends a JSON POST request with the contents of a file, passed with the filename as the second argument
echo "$(cat "$2" | sed 's/,\s*($|})/\\1/g')" | curl -s -H "Content-Type: application/json" -d @- "$1"
