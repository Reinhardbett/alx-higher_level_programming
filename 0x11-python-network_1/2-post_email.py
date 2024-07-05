#!/usr/bin/python3
''' Take in URL and email, send POST request, use email
as parameter, and display response.
Response should be decoded in utf-8
'''
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    '''Encode data to be sent'''
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')
    '''Create request object'''
    req = urllib.request.Request(sys.argv[1], data=encoded_data, method='POST')
    '''Send request and decode the response'''
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
