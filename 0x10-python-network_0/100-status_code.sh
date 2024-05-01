#!/bin/bash
# display the reponse in case of state 200
curl -s -w '%{response_code}' $1
