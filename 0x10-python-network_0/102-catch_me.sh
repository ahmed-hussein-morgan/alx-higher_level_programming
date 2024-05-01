#!/bin/bash
# make a request to 0.0.0.0:5000/catch_me respond with a message containing You got me!
curl -s 0.0.0.0:5000/catch_me | grep -q "You got me!" && printf "You got me!\n"
