from logic_layer.users_logic import create_user
from logic_layer.users_logic import get_user

# Test for success create user
def test_can_add_user():
    create_user_response, user_name_password = create_user()
    assert create_user_response.status_code == 200, "Can`t create user"
    data = create_user_response.json()
    print(data)
    user_name = data['data']
    print(user_name)
    get_user_response = get_user(user_name)
    assert get_user_response.status_code == 200, "Not found the user"

    get_userName = get_user_response.json()['data']['user_name']
    assert get_userName == user_name
