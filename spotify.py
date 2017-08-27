import requests
import json

def add_tracks_to_playlist(track_ids, access_token):
    uris = get_spotifyuri_list_from_track_ids(track_ids)
    add_tracks_to_playlist_url = lambda uris:"https://api.spotify.com/v1/users/savvasstephanides/playlists/5ma1IZtNj6bZ2EGu7KO0GV/tracks?uris=" + ",".join(uris)
    response = requests.post(add_tracks_to_playlist_url(uris), headers = {"Authorization":"Bearer " + access_token})
    return response.text

def get_spotifyuri_list_from_track_ids(track_ids):
    spotifyuris = []
    for track_id in track_ids:
        uri = get_spotifyuri_from_track_id(track_id)
        spotifyuris.append(uri)
    return spotifyuris

def get_spotifyuri_from_track_id(track_id):
    return "spotify:track:" + track_id


def get_track_ids_from_album(album_id, access_token):
    track_data = json.loads(get_album_raw_data(album_id, access_token))
    items = track_data["items"]
    track_ids = []
    for item in items:
        track_ids.append(item["id"])
    return track_ids

def get_album_raw_data(album_id, access_token):
    album_tracks_url = "https://api.spotify.com/v1/albums/" + album_id + "/tracks"
    response = requests.get(album_tracks_url, headers = {"Authorization":"Bearer " + access_token})
    return response.text