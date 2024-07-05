#!/usr/bin/python3
''' fetch status of url
'''
import urllib.request

if __name__ == "__main__":
    ''' Ensure file cannot execute when imported
    '''
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')\
            as response:
        status = response.read()
        decoded_status = status.decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(status)))
        print("\t- content: {}".format(status))
        print("\t- utf8 content: {}".format(decoded_status))
