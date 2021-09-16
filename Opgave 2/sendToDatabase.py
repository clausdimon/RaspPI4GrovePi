import json
import requests

def send():

    json_data = None

    with open('data.txt') as json_file:
        json_data = json.load(json_file)

    auth =('test', 'test')

    r = requests.post("https://10.130.54.67:5000/Temperatures", json =json_data, auth=auth)

    f = open('data.txt', 'r+')
    f.seek(0)
    f.truncate()
