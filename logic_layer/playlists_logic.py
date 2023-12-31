from infrastructure_layer import api


# Test for successfully add song to user`s playlist
def new_playlist_payload(user_name, user_password, song_title):
    return {
        "playlist_name": "The best of the best of the best",
        "song_title": song_title,
        "user_name": user_name,
        "user_password": user_password
    }

def add_song_to_playlist(user_name, user_password, song_title):
    payload = new_playlist_payload(user_name, user_password, song_title)
    return api.post("/playlists/add_song", payload)



