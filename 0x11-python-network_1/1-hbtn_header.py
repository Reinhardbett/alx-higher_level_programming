#!/usr/bin/python3
''' Take URL passed as arg and display value of X-Request-Id
'''
import urllib.request
import sys

if __name__ == "__main__":
    ''' request X-Request-Id variable from URL header
    '''
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
