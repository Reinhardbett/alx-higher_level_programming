#!/usr/bin/python3
''' Fetch URL using package requests
'''
import requests

if __name__ == "__main__":
    ''' Display formatted status
    '''
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
