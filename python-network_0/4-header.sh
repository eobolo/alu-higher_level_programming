#!/bin/bash
# Send the GET request with the specified header, display the entire response headers, and extract the reason phrase
curl -s -I -X GET -H "X-HolbertonSchool-User-Id: 98" "$1" | grep -i 'HTTP/1.1' | awk '{print $2}'
