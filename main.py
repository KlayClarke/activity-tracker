import os
from datetime import datetime
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

today = datetime.now()
pixel_creation_params = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '2',
}

pixel_update_endpoint = f'{pixel_creation_endpoint}/20211128'

pixel_update_params = {
    'quantity': '4',
}

pixel_delete_endpoint = f'{pixel_update_endpoint}'

response = requests.delete(url=pixel_update_endpoint, headers=headers)
print(response.text)
