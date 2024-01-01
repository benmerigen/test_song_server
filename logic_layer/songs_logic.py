import uuid

from infrastructure_layer import api
from logic_layer.users_logic import create_user


def create_song(song_genre, song_performer, song_title, song_year):
    payload = {
        'song_genre': song_genre,
        'song_performer': song_performer,
        'song_title': song_title,
        'song_year': song_year
    }
    return api.post("/songs/add_song", payload)


def get_song(song_name):
    params = {'song_title': song_name}
    return api.get("/songs/get_song", params)

def add_upvote(playlistName_NotRelevant, test_song_title, test_username, test_password):
    payload = {
        'playlist_name': playlistName_NotRelevant,
        'song_title': test_song_title,
        'user_name': test_username,
        'user_password': test_password
    }
    return api.put("/songs/upvote", payload)

def down_vote(playlistName_NotRelevant, test_song_title, test_username, test_password):
    payload = {
        'playlist_name': playlistName_NotRelevant,
        'song_title': test_song_title,
        'user_name': test_username,
        'user_password': test_password
    }
    return api.put("/songs/downvote", payload)


# build 3 songs and user and voting them
def build_songs_for_test():
    create_user("Arnold", "topsicrt") # create user for voting
    for i in range(1,6): # create 5 songs
        create_song("test_song_genre", "test_song_performer", f"test_song_title_{i}", 1990)
    song_num = 1
    for j in range(13, 22, 2): # add votes to the song (13, 15, 17)
        add_vote(j, "not_relevant", f"test_song_title_{song_num}", "Arnold", "topsicrt")
        song_num += 1

# temp_function for build songs
def add_vote(numberOfVotes, playlist_name, song_title, user_name, user_password): # temp_function for build songs
    for i in range (numberOfVotes):
        add_upvote(playlist_name, song_title, user_name, user_password)

def search_for_songs (rank, op):
    params = {
        "rank": rank,
        "op": op
    }
    return api.get("/songs/ranked_songs", params)

def delete_db_songs_data():
    return api.delete("/admin/delete_all_songs")