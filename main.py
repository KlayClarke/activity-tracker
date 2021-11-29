import os
import requests

PIXELA_TOKEN = os.environ.get('PIXELA_TOKEN')
pixela_endpoint = 'https://pixe.la/v1/users'

pixela_params = {
    'token': PIXELA_TOKEN,
    'username': 'klayaclarke',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

pixela_response = requests.post(url=pixela_endpoint, json=pixela_params,)

print(pixela_response.text)