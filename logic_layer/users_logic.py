import uuid
from infrastructure_layer import api


def new_user_payload():
    user_name = f"test_user_name_{uuid.uuid4().hex}"
    user_password = f"test_user_password_{uuid.uuid4().hex}"

    return {
        "user_name": user_name,
        "user_password": user_password
    }


def create_user():
    payload = new_user_payload()
    response = api.post("/users/add_user", payload)
    return response, payload["user_password"]


def get_user(user_name):
    params = {'user_name': user_name}
    return api.get("/users/get_user", params)


def delete_db_users_data():

