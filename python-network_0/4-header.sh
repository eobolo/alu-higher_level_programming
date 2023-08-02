#!/bin/bash
# Send the GET request with the specified header and display the body of the response
curl -sL -H "X-HolbertonSchool-User-Id: 98" "$1"
