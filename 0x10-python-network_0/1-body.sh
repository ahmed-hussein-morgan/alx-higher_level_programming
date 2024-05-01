#!/bin/bash
# desplay the reponse in case of state 200
curl -s $1 | grep "200"
