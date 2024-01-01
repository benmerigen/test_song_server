import pytest

from logic_layer.playlists_logic import add_song_to_playlist
from logic_layer.songs_logic import create_song
from logic_layer.users_logic import create_user, get_user, create_playlist


# Test add song to playlist successfully
@pytest.mark.parametrize(("song_genre", "song_performer", "song_title", "song_year", "user_name", "user_password", "playlist_name"),
                         [
                             ("Rock", "Creedence Clearwater Revival", "test_song_name", 1970, "Arnold1", "topsicret", "test_playlist")
                         ])
def test_can_add_song_to_playlist(set_up_data_base, song_genre, song_performer, song_title, song_year,user_name, user_password, playlist_name):
    create_song_response = create_song(song_genre, song_performer, song_title, song_year)
    assert create_song_response.status_code == 200, "Can`t create song"
    create_user_response = create_user(user_name, user_password)
    assert create_user_response.status_code == 200, "Can`t create user"
    create_playlist_response = create_playlist(playlist_name, user_name, user_password)
    assert create_playlist_response.status_code == 200, "Can`t create playlist"

    add_song_to_playlist_response = add_song_to_playlist(playlist_name,song_title, user_name, user_password)
    assert add_song_to_playlist_response.status_code == 200, "Can`t add song to playlist"

    get_user_response = get_user(user_name)

    assert get_user_response.status_code == 200, "Not found the user "

    assert len(get_user_response.json()['data']['playlists']) == 1, "This is not add song to playlist "



# Test add song to playlist that already exist
@pytest.mark.parametrize(("song_genre", "song_performer", "song_title", "song_year", "user_name", "user_password", "playlist_name"),
                         [
                             ("Rock", "Creedence Clearwater Revival", "test_song_name", 1970, "Arnold1", "topsicret", "test_playlist")
                         ])
def test_add_exist_song_to_playlist(set_up_data_base, song_genre, song_performer, song_title, song_year,user_name, user_password, playlist_name):
    create_song(song_genre, song_performer, song_title, song_year)
    create_user(user_name, user_password)
    create_playlist(playlist_name, user_name, user_password)
    add_song_to_playlist(playlist_name, song_title, user_name, user_password) # add song
    add_song_to_playlist_response = add_song_to_playlist(playlist_name, song_title, user_name, user_password) # add song that already exist
    assert add_song_to_playlist_response.json()['error'] == "the song test_song_name already exist in the playlist or not in the songs collection"

# Test to add song to playlist that song doesnt exist
@pytest.mark.parametrize(("song_title", "user_name", "user_password", "playlist_name"),
                         [
                             ("test_song_name", "Arnold1", "topsicret", "test_playlist")
                         ])
def test_add_doesnt_exist_song_to_playlist(set_up_data_base, song_title,user_name, user_password, playlist_name):
    create_user(user_name, user_password)
    create_playlist(playlist_name, user_name, user_password)
    add_song_to_playlist(playlist_name, song_title, user_name, user_password) # add song
    add_song_to_playlist_response = add_song_to_playlist(playlist_name, song_title, user_name, user_password) # add song that already exist
    assert add_song_to_playlist_response.json()['error'] == "the song test_song_name already exist in the playlist or not in the songs collection"


# Test to add song to playlist that doesnt exist
@pytest.mark.parametrize(("song_genre", "song_performer", "song_title", "song_year", "user_name", "user_password", "playlist_name"),
                         [
                             ("Rock", "Creedence Clearwater Revival", "test_song_name", 1970, "Arnold1", "topsicret", "test_playlist")
                         ])
def test_add_song_to_playlist_doesnt_exist(set_up_data_base, song_genre, song_performer, song_title, song_year,user_name, user_password, playlist_name):
    create_song(song_genre, song_performer, song_title, song_year)
    create_user(user_name, user_password)
    add_song_to_playlist(playlist_name, song_title, user_name, user_password) # add song
    add_song_to_playlist_response = add_song_to_playlist(playlist_name, song_title, user_name, user_password) # add song that already exist
    assert add_song_to_playlist_response.json()['error'] == "the song test_song_name already exist in the playlist or not in the songs collection"


q