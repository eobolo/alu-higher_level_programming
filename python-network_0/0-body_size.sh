#!/bin/bash

# Check if the URL argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

url="$1"

# Send the request using curl and output the size of the response body in bytes
filesize=$(curl -s -w '%{size_download}' -o /dev/null "$url")

# Display the size of the response body in bytes
echo "$filesize"
