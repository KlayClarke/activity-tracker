import os
import requests

USERNAME = 'klayaclarke'
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
    'id': 'graph1',
    'name': 'Programming Graph',
    'unit': 'hour',
    'type': 'float',
    'color': 'sora'
}

response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(response.text)
