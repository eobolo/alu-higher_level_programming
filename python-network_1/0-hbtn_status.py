#!/usr/bin/python3
# 0-hbtn_status.py
"""This module or script
fetches https://alu-intranet.hbtn.io/status
using the urllib library
"""


import urllib.request


url = "https://alu-intranet.hbtn.io/status"
request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    print(response.read())
