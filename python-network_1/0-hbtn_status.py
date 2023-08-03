#!/usr/bin/python3
# 0-hbtn_status.py
"""This module or script
fetches https://alu-intranet.hbtn.io/status
using the urllib library
"""


import urllib.request


url = 'https://alu-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    response_body = response.read()
    response_text = response_body.decode('utf-8')
    print("Body response:")
    print("\t- type:", type(response_body))
    print("\t- content:", response_body)
    print("\t- utf8 content:", response_text)
