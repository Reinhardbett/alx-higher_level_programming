#!/usr/bin/python3
''' Send POST request with email as param and display response
'''
import requests
import sys

if __name__ == "__main__":
    '''pass email as param to POST request'''
    data = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=data)
    print(r.text)
