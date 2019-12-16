import requests
# Get requests
# DO not have a body (JSON)
# They have a base url

base_url = 'http://api.postcodes.io/'
path = 'postcodes/'
arguments = 'e146gt'

request_response = requests.get(base_url + path + arguments)
# Check connection is good
print(request_response)

# Turning a request into dictionary --> use .json()
dictionary_response = request_response.json()
print(dictionary_response['result']['admin_ward'])

