import requests
import json
import time
from post_function import *

# Making POST requests

# We need a path
base_url = 'http://api.postcodes.io/'
path = 'postcodes/'

## While loop which gets postcode and nhs location

# while True:
#     p1 = input('Postcode: ')
#     p2 = input('Postcode: ')
#     p3 = input('Postcode: ')
#     dictionary_post_codes = {
#         'postcodes': [f'{p1}', f'{p2}', f'{p3}']
#     }
#     json_body = json.dumps(dictionary_post_codes)
#     headers = {'Content-type': 'application/json'}
#     postcodes_post_response = requests.post(base_url + path, data=json_body, headers=headers)
#     results = postcodes_post_response.json()['result']
#     a = 0
#     for request in results:
#         a += 1
#         print(f'> {a} - Postcode:', request['result']['postcode'], '- with nhs location at:', request['result']['nhs_ha'])
#         time.sleep(1)
#     break


# While loop which asks what information they are looking for

while True:
    user_input = input('Do you want to look up some postcodes? (y/n) ')
    if user_input == 'y':
        p1 = input('Postcode: ')
        p2 = input('Postcode: ')
        p3 = input('Postcode: ')
        dictionary_post_codes = {
            'postcodes': [f'{p1}', f'{p2}', f'{p3}']
        }
        arguments = f'{p1}'
        request_response = requests.get(base_url + path + arguments)
        winning = request_response.json()
        results = post_function(dictionary_post_codes).json()['result']
        for keys in winning['result'].keys():
            print('>', keys)
        while True:
            a = 0
            user_input = input('\nWhat would you like to look at from the list of keys? Or type exit to return to beginning ').strip()
            if user_input == 'exit':
                break
            else:
                for request in results:
                    a += 1
                    print(f'> {a} - Postcode:', request['result']['postcode'],f'-- {user_input}:', request['result'][f'{user_input}'])
                    time.sleep(1)
    elif user_input == 'n':
        break
    else:
        print('Not a valid option')
        continue







