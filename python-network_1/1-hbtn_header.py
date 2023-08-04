#!/usr/bin/python3
# 0-hbtn_status.py
"""This module or script
fetches https://alu-intranet.hbtn.io/status
using the urllib library
"""


from urllib import request, error
import sys
"""This module or script
fetches https://alu-intranet.hbtn.io/status
using the urllib library
"""


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
