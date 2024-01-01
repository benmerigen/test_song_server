import os
import requests
import configparser

# get the absolute path of the directory containing this script
current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, 'config.ini')

config = configparser.ConfigParser()
config.read(config_path)
address = config['SERVER'].get('address')
port = config['SERVER'].get('port')
url = f'http://{address}:{port}'

print(config.sections())
print(address)


def get(endpoint, params):
    request = requests.get(url + endpoint, params=params)
    return request



def post(endpoint, msg):
    request = requests.post(url + endpoint, json=msg)
    return request


def put(endpoint, msg):
    request = requests.put(url + endpoint, json=msg)
    return request


def delete(endpoint):
    request = requests.delete(url + endpoint)
    return request
