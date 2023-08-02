#!/bin/bash
# Send the GET request with the specified header, display the body of the response, and extract "OK"
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" "$1" | awk '/^\r?$/ { body=1; next } body { print }' | grep -o 'OK'
