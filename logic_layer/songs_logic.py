import uuid

from infrastructure_layer import api


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

def delete_db_songs_data():
    return api.delete("/admin/delete_all_songs")