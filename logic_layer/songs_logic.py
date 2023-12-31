import uuid

from infrastructure_layer import api


# def new_song_payload():


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



def delete_db_songs_data():
