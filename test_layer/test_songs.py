import pytest

from logic_layer.songs_logic import create_song, get_song, add_upvote, build_songs_for_test, search_for_songs, down_vote
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

# Test for successfully downvote
def test_downvote_song(set_up_data_base):
    create_song("test_song_genre", "test_song_performer", "test_song_title", 1990)
    create_user("test_username", "test_password")
    add_upvote("playlistName_NotRelevant", "test_song_title", "test_username", "test_password")
    # already checked that 3 actions above

    create_downvote_response = down_vote("playlistName_NotRelevant", "test_song_title", "test_username", "test_password")
    assert create_downvote_response.status_code == 200, "Can`t down vote to this song"
    assert create_downvote_response.json()['data']['rating'] == 0 # the down vote happened

# Test for downvote do not down under 0
def test_check_downvote_zero(set_up_data_base):
    create_song("test_song_genre", "test_song_performer", "test_song_title", 1990)
    create_user("test_username", "test_password")
    for i in range(4):
        create_downvote_response= down_vote("playlistName_NotRelevant", "test_song_title", "test_username","test_password")
    assert create_downvote_response.json()['data']['rating'] == 0  # the rating is still zero







# Test to get songs with low\high\equal rating than x
def test_search_by_rating(set_up_data_base):
    build_songs_for_test()
    rating = 17 # rating for filter
    less_rating_response = search_for_songs(rating, "less")
    for i in range(1,3):
        searh_by_rating(f"test_song_title_{i}", less_rating_response.json()['data'])

    eq_rating_response = search_for_songs(rating, "eq")
    assert "test_song_title_3" in eq_rating_response.json()['data']

    greater_rating_response = search_for_songs(rating, "greater")
    for i in range(4,6):
        searh_by_rating(f"test_song_title_{i}", greater_rating_response.json()['data'])

def searh_by_rating(song_tile, data):
    assert song_tile in data





