#!/usr/bin/python3
''' Fetch URL using package requests
'''
import requests

if __name__ == "__main__":
    ''' Display formatted status
    '''
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: ", type(response.text))
    print("\t- content: ", response.text)
