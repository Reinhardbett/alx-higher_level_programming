#!/usr/bin/python3
''' Take URL, send request, and display header variable
'''
import requests
import sys

if __name__ == "__main__":
    '''Send request'''
    r = requests.get(sys.argv[1])
    '''Retrieve value of key X-Request-Id'''
    print(r.headers.get('X-Request-Id'))
