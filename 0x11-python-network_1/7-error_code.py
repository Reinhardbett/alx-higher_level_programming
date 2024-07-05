#!/usr/bin/python3
''' Take URL passed as arg, send request, and display response
'''
import requests
import sys

if __name__ == "__main__":
    '''send request and check status code'''
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
