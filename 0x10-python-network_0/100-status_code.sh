#!/bin/bash
# display the reponse in case of state 200
curl -s --write-out %{http_connect} $1
