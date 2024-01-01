from infrastructure_layer import api


def create_user(user_name, user_password):
    payload = {
        "user_name": user_name,
        "user_password": user_password
    }
    response = api.post("/users/add_user", payload)
    return response


def get_user(user_name):
    params = {'user_name': user_name}
    return api.get("/users/get_user", params)

def create_friend(user_name, user_password, friend_name):
    payload = {
        "user_name": user_name,
        "user_password": user_password,
        "friend_name": friend_name
    }
    return api.put("/users/add_friend", payload)

def create_playlist(playlist_name, user_name, user_password):
    payload = {
        "playlist_name": playlist_name,
        "user_name": user_name,
        "user_password": user_password
    }
    return api.post("/users/add_playlist", payload)

def get_playlist(playlist_name, user_name, user_password):
    params = {
        "playlist_name": playlist_name,
        "user_name": user_name,
        "user_password": user_password
    }
    return api.get("/users/get_playlist", params)


def delete_db_users_data():
    return api.delete("/admin/delete_all_users")


