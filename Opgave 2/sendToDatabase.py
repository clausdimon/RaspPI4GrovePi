import json
import requests
from requests.models import HTTPBasicAuth

def send():

    json_data = None

    with open('data.json', 'r') as json_file:
        json_data = json.load(json_file)

    auth =HTTPBasicAuth('test', 'test')
    header = {
        'content-type': 'application/json',
        'accept': 'application/json'
    }

    r = requests.post("https://10.130.54.67:5000/Temperatures", json=json_data, headers=header, auth=auth, verify=False)

    dataTemp = []

    with open('data.json', "w" ) as file:
        json.dump(dataTemp, file)
