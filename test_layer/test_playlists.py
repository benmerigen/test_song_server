import pytest

from logic_layer.playlists_logic import add_song_to_playlist
from logic_layer.songs_logic import create_song
from logic_layer.users_logic import create_user, get_user


# Test add song to playlist but its not work
@pytest.mark.parametrize(("song_genre", "song_performer", "song_title", "song_year", "user_name", "user_password"),
                         [
                             ("Rock", "Creedence Clearwater Revival", "test_song_name", 1970, "Arnold", "topsicret")
                         ])
@pytest.mark.xfail
def test_can_add_song_to_playlist(set_up_data_base, song_genre, song_performer, song_title, song_year,user_name, user_password):
    create_song_response = create_song(song_genre, song_performer, song_title, song_year)
    assert create_song_response.status_code == 200, "Can`t create song"
    create_user_response, user_name_password = create_user(user_name, user_password)
    assert create_user_response.status_code == 200, "Can`t create user"

    song_name = create_song_response.json()['data']
    user_name = create_user_response.json()['data']

    add_song_to_playlist_response = add_song_to_playlist(user_name, user_name_password, song_name)
    assert add_song_to_playlist_response.status_code == 200, "Can`t add song to playlist"

    get_user_response = get_user(user_name)

    assert get_user_response.status_code == 200, "Not found the user "

    assert len(get_user_response.json()['data']['playlists']) == 1, "This is not add song to playlist "



