#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.

Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""


import urllib.request
import urllib.error
import sys

def fetch_and_display_url_body(url):
    """
    Fetches the body of a URL response and displays it.

    Args:
        url (str): The URL to fetch the response from.

    Returns:
        str: The decoded body of the response.

    Raises:
        urllib.error.HTTPError: If an HTTP error occurs (e.g., 404, 500).
    """
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print("Response Body:")
            print(body)
            return body
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
        return ""

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <url>")
    else:
        url = sys.argv[1]
        fetch_and_display_url_body(url)
