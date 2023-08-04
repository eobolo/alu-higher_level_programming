#!/usr/bin/python3
"""
This module is a script that fetches https://alu-intranet.hbtn.io/status
using the urllib library and displays the value of the X-Request-Id
variable found in the header of the response.
"""

from urllib import request, error
import sys

try:
    url = sys.argv[1]
    with request.urlopen(url) as response:
        print(response.headers['X-Request-Id'])
except error.URLError:
    custom_status = bytes("Custom status", encoding="utf-8")
    custom_status_text = custom_status.decode('utf-8')
    print("Body response:")
    print("\t- type:", type(custom_status))
    print("\t- content:", custom_status)
    print("\t- utf8 content:", custom_status_text)
