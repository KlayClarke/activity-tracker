import os
import requests

USERNAME = 'klayaclarke'
GRAPH_ID = 'graph1'
TOKEN = os.environ.get('PIXELA_TOKEN')

headers = {
    'X-USER-TOKEN': TOKEN
}

pixela_endpoint = 'https://pixe.la/v1/users'

pixela_params = {
    'token': TOKEN,
    'username': 'klayaclarke',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_params = {
    'id': GRAPH_ID,
    'name': 'Programming Graph',
    'unit': 'hour',
    'type': 'float',
    'color': 'sora'
}

pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

pixel_creation_params = {
    'date': '20211129',
    'quantity': '3.5',
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_creation_params, headers=headers)
print(response.text)
