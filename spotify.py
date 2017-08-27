import requests

def add_tracks_to_playlist(track_ids, access_token):
    uris = get_spotifyuri_list_from_track_ids(track_ids)
    add_tracks_to_playlist_url = lambda uris:"https://api.spotify.com/v1/users/savvasstephanides/playlists/5ma1IZtNj6bZ2EGu7KO0GV/tracks?uris=" + ",".join(uris)
    response = requests.post(add_tracks_to_playlist_url(uris), headers = {"Authorization":"Bearer " + access_token})
    print(response.text)

def get_spotifyuri_list_from_track_ids(track_ids):
    spotifyuris = []
    for track_id in track_ids:
        uri = get_spotifyuri_from_track_id(track_id)
        spotifyuris.append(uri)
    return spotifyuris

def get_spotifyuri_from_track_id(track_id):
    return "spotify:track:" + track_id


