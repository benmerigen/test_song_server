import uuid

import requests

from infrastructure_layer.api import ENDPOINT


def new_song_payload():
    song_name = f"test_song_name_{uuid.uuid4().hex}"

    return {
        "song_genre": "Roc1k",
        "song_performer": "Creedence Clearwater Revival",
        "song_title": song_name,
        "song_year": 1970
    }

def create_song():
    payload = new_song_payload()
    return requests.post(ENDPOINT + "/songs/add_song", json=payload)


def get_song(song_name):
    params = {'song_title': song_name}
    return requests.get(ENDPOINT + f"/songs/get_song", params=params)