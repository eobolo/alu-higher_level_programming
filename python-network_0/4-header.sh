#!/bin/bash
# Send the GET request with the specified header, display the response headers, and extract the reason phrase
curl -s -I -X GET -H "X-HolbertonSchool-User-Id: 98" "$1" | grep 'HTTP/1.1' | awk '{ print $2 }'
