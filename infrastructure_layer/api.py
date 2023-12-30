import requests

ENDPOINT = 'http://127.0.0.1:3002'

def get_endpoint():
    response = requests.get(ENDPOINT)
    return response
