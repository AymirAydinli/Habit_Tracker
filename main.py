import requests
import os
from dotenv import load_dotenv
import datetime as dt

load_dotenv()

pixela_endpoint = os.getenv('pixela_endpoint')
token = os.getenv('user_token')
username = 'aymir'
user_params = {
    'token': token,
    'username': username,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response_user = requests.post(url=pixela_endpoint, json=user_params)
# print(response_user.text)

graph_endpoint = f'{pixela_endpoint}/{username}/graphs'
graph_params = {
    'id': 'graph1',
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'ajisai'
}

headers = {
    "X-USER-TOKEN": token
}

# response_graph = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response_graph.text)


pixel_url = f'{graph_endpoint}/{graph_params["id"]}'

today = dt.datetime.today().date()
today_date = today.strftime('%Y%m%d')




pixel_params = {
    'date': today_date,
    'quantity': '10'
}

#response_pixel = requests.post(url=pixel_url, json=pixel_params, headers=headers)


pixel_update_url = f'{graph_endpoint}/{graph_params["id"]}/{today_date}'


pixel_update_params = {
    'quantity': '20'
}

response_pixel_update = requests.put(url=pixel_update_url, json=pixel_update_params, headers=headers)



