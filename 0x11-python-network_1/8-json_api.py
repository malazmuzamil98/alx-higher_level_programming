#!/usr/bin/python3
"""
Script that takes a letter as input, sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter,
and processes the response.
"""
import requests
import sys

if __name__ == "__main__":
    q = "" if (len(sys.argv) == 1) else sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}
    response = requests.post(url, data=data)

    try:
        json_response = response.json
        if json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No Result")
    except ValueError:
        print("Not a valid JSON")
