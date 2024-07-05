#!/usr/bin/python3
'''Take in letter, send POST request using letter as param
'''
import requests
import sys

if __name__ == "__main__":
    '''Accept and verify letter input'''
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    '''Send POST request with letter parameter'''
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        r_json = r.json()
        if r_json:
            '''Assuming result is a dict'''
            print("[{}] {}".format(r_json.get("id"), r_json.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
