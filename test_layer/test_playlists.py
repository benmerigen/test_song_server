from logic_layer.playlists_logic import add_song_to_playlist
from logic_layer.songs_logic import create_song
from logic_layer.users_logic import create_user


def test_can_add_song_to_playlist():
    create_song_response = create_song()
    assert create_song_response.status_code == 200, "Can`t create song"

    create_user_response, user_name_password = create_user()
    assert create_user_response.status_code == 200, "Can`t create user"

    song_name = create_song_response.json()['data']
    user_name = create_user_response.json()['data']

    add_song_to_playlist_response = add_song_to_playlist(user_name, user_name_password, song_name)
    assert add_song_to_playlist_response.status_code == 200, "Can`t add song to playlist"


