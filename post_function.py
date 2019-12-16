import json
import requests

base_url = 'http://api.postcodes.io/'
path = 'postcodes/'

def post_function(arg):
    json_body = json.dumps(arg)
    headers = {'Content-type': 'application/json'}
    return requests.post(base_url + path, data=json_body, headers=headers)