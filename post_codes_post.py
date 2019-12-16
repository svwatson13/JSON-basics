import requests
import json
import time

# Making POST requests

# We need a path
base_url = 'http://api.postcodes.io/'
path = 'postcodes/'

# Creating json
dictionary_post_codes = {
    'postcodes': ['EC2Y 5AS', 'E146GT', 'CT1 2EH']
}

json_body = json.dumps(dictionary_post_codes)

# Possibly headers, depending on the api
headers = {'Content-type': 'application/json'}


# Making the request
postcodes_post_response = requests.post(base_url+path, data=json_body, headers = headers)

print(postcodes_post_response.json())

results = postcodes_post_response.json()['result']
for request in results:
    print(request)
    print(request['result']['admin_ward'])
    time.sleep(1)
