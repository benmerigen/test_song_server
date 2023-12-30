import uuid

import requests

from infrastructure_layer.api import ENDPOINT


def new_user_payload():
    user_name = f"test_user_name_{uuid.uuid4().hex}"
    user_password = f"test_user_password_{uuid.uuid4().hex}"

    return {
        "user_name": user_name,
        "user_password": user_password
    }


def create_user():
    payload = new_user_payload()
    response = requests.post(ENDPOINT + "/users/add_user", json=payload)
    return response, payload["user_password"]


def get_user(user_name):
    params = {'user_name': user_name}
    return requests.get(ENDPOINT + f"/users/get_user", params=params)
