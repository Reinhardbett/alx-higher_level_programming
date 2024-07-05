#!/usr/bin/python3
''' Take URL passed as arg, send request, display dcoded response
Manage HTTPError exception
'''
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    '''display response to GET request
    manage HTTPError
    '''
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
