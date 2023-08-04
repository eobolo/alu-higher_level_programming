#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    # Get the URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Create a POST request using the URL and encoded data
    request = urllib.request.Request(url, data=data, method='POST')

    # Send the request and handle the response
    with urllib.request.urlopen(request) as response:
        # Read and decode the body of the response
        response_body = response.read().decode('utf-8')

        # Print the decoded response
        print(response_body)
