from logic_layer.users_logic import create_user, create_friend, create_playlist, get_playlist
from logic_layer.users_logic import get_user
import pytest

@pytest.mark.parametrize(("user_name", "user_password"),
                         [
                             ("Arnold", "topsicret")
                         ])
# Test for success create user
def test_can_add_user(set_up_data_base, user_name, user_password):
    create_user_response = create_user(user_name, user_password)
    assert create_user_response.status_code == 200, "Can`t create user"
    data = create_user_response.json()
    user_name = data['data']

    get_user_response = get_user(user_name)
    assert get_user_response.status_code == 200, "Not found the user"

    get_userName = get_user_response.json()['data']['user_name']
    assert get_userName == user_name


# Test for create user with empty values - IF IT IS RELEVANT
@pytest.mark.parametrize(("user_name", "user_password"),
                         [
                            ("", "topsicret"),
                            ("Ben", "")
                         ])
@pytest.mark.xfail
def test_add_empty_user(set_up_data_base, user_name, user_password):
    create_user_response = create_user(user_name, user_password)
    assert create_user_response.status_code != 200, "Create user"


# Test that success to add friend to user
@pytest.mark.parametrize(("user_name", "user_password", "friend_name"),
                         [
                             ("Arnold", "topsicret" , "Friend")
                         ])
def test_add_friend_user(set_up_data_base, user_name, user_password, friend_name):
    create_user_response = create_user(user_name, user_password)
    assert create_user_response.status_code == 200, "Can`t create user"

    create_friend_response = create_friend(user_name, user_password, friend_name)
    create_friend_response.status_code == 200, "Can`t add friend"

    get_user_response = get_user(user_name)
    assert len(get_user_response.json()['data']['friends']) == 1



# Test that try to add friend to user with wrong password
@pytest.mark.parametrize(("user_name", "user_password"),
                         [
                             ("wrong_user", "Test_password"),
                             ("Test_user", "sdffsd")
                         ])
def test_add_friend_wrong_input_user(set_up_data_base, user_name, user_password):
    create_user_response = create_user("Test_user", "Test_password")
    assert create_user_response.status_code == 200, "Can`t create user"

    create_friend_response = create_friend(user_name, user_password, "Test_friend")
    assert create_friend_response.status_code == 200, "Can`t add friend"

    print(create_friend_response.json().get('error'))
    if create_friend_response.json().get('error'):
        assert True
        return # there is response with error, dont continue to assert false
    assert False


# Test check that user successfully create new playlist
@pytest.mark.parametrize(("playlist_name", "user_name", "user_password"), [("test_play","Arnold", "topsicrt")])
def test_add_new_playlist(set_up_data_base, playlist_name, user_name, user_password):
    create_user_response = create_user(user_name, user_password)
    assert create_user_response.status_code == 200, "Can`t create user"

    create_playlist_response = create_playlist(playlist_name, user_name, user_password)
    assert create_playlist_response.status_code == 200, "Can`t create playlist"

    get_playlist_response = get_playlist(playlist_name, user_name, user_password)
    assert get_playlist_response.status_code == 200, "Can`t find the playlist"



# Test to check create exist playlist
@pytest.mark.parametrize(("playlist_name", "user_name", "user_password"), [("test_play","Arnold", "topsicrt")])
def test_add_exist_playlist(set_up_data_base, playlist_name, user_name, user_password):
    create_user_response = create_user(user_name, user_password)
    assert create_user_response.status_code == 200, "Can`t create user"
    create_playlist(playlist_name, user_name, user_password) # create playlist first time
    create_playlist_response = create_playlist(playlist_name, user_name, user_password) # playlist exist
    assert create_playlist_response.json().get('error') # get error message







