from logic_layer.songs_logic import create_song
from logic_layer.songs_logic import get_song


# Test for success add song
def test_can_add_song():
    create_song_response = create_song()
    assert create_song_response.status_code == 200, "Can`t create song"

    data = create_song_response.json()
    print(data)
    song_name = data['data']
    print(song_name)
    get_song_response = get_song(song_name)
    assert get_song_response.status_code == 200, "Not found the song"

    get_songName = get_song_response.json()['data']['title']
    assert get_songName == song_name