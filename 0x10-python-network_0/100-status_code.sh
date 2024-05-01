#!/bin/bash
# display the reponse in case of state
curl -s -o /dev/null -w "%{http_code}" "$1"
