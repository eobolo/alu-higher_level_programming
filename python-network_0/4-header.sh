#!/bin/bash
# Send the GET request with the specified header and display the body of the response
curl -siH "X-HolbertonSchool-User-Id: 98" "$1" | awk '/^\r?$/ { body=1; next } body { print }'
