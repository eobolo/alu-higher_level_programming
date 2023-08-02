#!/bin/bash
# Send the request using curl, and display the body of the response for 200 status code
curl -s -o /dev/null -w "%{http_code}" "$1" | [ "$(cat)" == "200" ] && curl -s "$1"
