#!/bin/bash
# sends a JSON POST request with the contents of a file, passed with the filename as the second argument
curl -s -F "@$2;type=json" $1 
