import pytest

from logic_layer.songs_logic import create_song, get_song, add_upvote
from logic_layer.users_logic import create_user


# Test for success add song
@pytest.mark.parametrize(("song_genre", "song_performer", "song_title", "song_year"),
                         [
                             ("Rock", "Creedence Clearwater Revival", "test_song_name", 1970)
                         ])
def test_can_add_song(set_up_data_base, song_genre, song_performer, song_title, song_year):
    create_song_response = create_song(song_genre, song_performer, song_title, song_year)
    assert create_song_response.status_code == 200, "Can`t create song"

    data = create_song_response.json()

    song_name = data['data']

    get_song_response = get_song(song_name)
    assert get_song_response.status_code == 200, "Not found the song"

    get_songName = get_song_response.json()['data']['title']
    get_songRating = get_song_response.json()['data']['rating']
    assert get_songName == song_name
    assert  get_songRating == 0


# Test try add song that already exist
@pytest.mark.parametrize(("song_genre", "song_performer", "song_title", "song_year"),
                         [
                             ("Rock", "Creedence Clearwater Revival", "test_song_name", 1970)
                         ])
def test_can_add_song(set_up_data_base, song_genre, song_performer, song_title, song_year):
    create_song(song_genre, song_performer, song_title, song_year) # first time
    create_song_response = create_song(song_genre, song_performer, song_title, song_year) # second time
    assert create_song_response.json()['error'] == "this song already exist in the collection"


# Test for create user with empty values - IF IT IS RELEVANT
@pytest.mark.parametrize(("song_genre", "song_performer", "song_title", "song_year"),
                         [
                             ("Test_genre", "test_per", "", 1970),
                             ("Test_genre", "", "test_title", 1970),
                             ("", "test_per", "test_title", 1970)
                         ])
@pytest.mark.xfail
def test_add_empty_input_song(set_up_data_base, song_genre, song_performer, song_title, song_year):
    create_song_response = create_song(song_genre, song_performer, song_title, song_year)
    assert create_song_response.status_code != 200, "Create Song"


# Test for successfully upvote - Manully parameters
def test_upvote_song(set_up_data_base):
    create_song("test_song_genre", "test_song_performer", "test_song_title", 1990)
    create_user("test_username", "test_password")
    create_upvote_response = add_upvote("playlistName_NotRelevant", "test_song_title","test_username", "test_password")
    assert create_upvote_response.status_code == 200, "Can`t up vote to this song"
    assert create_upvote_response.json()['data']['rating'] == 1

