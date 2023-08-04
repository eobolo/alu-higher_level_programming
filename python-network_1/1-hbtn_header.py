#!/usr/bin/python3
# 1-hbtn_header.py
"""This a python module
that takes a url and fetches
and display the value of an
header
"""


import urllib.request
import sys


url = sys.argv[1]
request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    print(response.headers["X-Request-Id"])
