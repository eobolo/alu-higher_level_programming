#!/bin/bash
# Send the GET request with the specified header and display the body of the response
curl -s -i "$1" | grep -E "HTTP" | awk '{print $3}'
