#!/bin/bash
# make a request to 0.0.0.0:5000/catch_me respond with a message containing You got me!
curl -s -o /dev/null -w "You got me! " 0.0.0.0:5000/catch_me
