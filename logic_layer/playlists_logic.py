from infrastructure_layer import api


# Test for successfully add song to user`s playlist
def new_playlist_payload(playlist_name, song_title, user_name, user_password):
    return {
        "playlist_name": playlist_name,
        "song_title": song_title,
        "user_name": user_name,
        "user_password": user_password
    }

def add_song_to_playlist(playlist_name, song_title, user_name, user_password):
    payload = new_playlist_payload(playlist_name, song_title, user_name, user_password)
    return api.post("/playlists/add_song", payload)



