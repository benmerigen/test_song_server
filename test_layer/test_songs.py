import pytest

from logic_layer.songs_logic import create_song
from logic_layer.songs_logic import get_song


# Test for success add song
@pytest.mark.parametrize(("song_genre", "song_performer", "song_title", "song_year"),
                         [
                             ("Rock", "Creedence Clearwater Revival", "test_song_name", 1970)
                         ])
def test_can_add_song(song_genre, song_performer, song_title, song_year):
    create_song_response = create_song(song_genre, song_performer, song_title, song_year)
    assert create_song_response.status_code == 200, "Can`t create song"

    data = create_song_response.json()
    print(data)
    song_name = data['data']
    print(song_name)
    get_song_response = get_song(song_name)
    assert get_song_response.status_code == 200, "Not found the song"

    get_songName = get_song_response.json()['data']['title']
    assert get_songName == song_name

    #
    #  check requirment of rating 0 in new song
    #
