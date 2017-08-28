import spotify_configuration
import reddit
import spotify
import spotify_auth_refresh
import datetime
def run_playlist_creation():
    print("Date: " + str(datetime.datetime.today()))
    access_token = get_access_token()
    spotify.clear_playlist(access_token)
    print("Playlist cleared!")
    track_ids = get_track_ids(access_token)
    spotify.add_tracks_to_playlist(track_ids, access_token)
    print(str(len(track_ids)) + " new tracks added!")

def get_access_token():
    access = spotify_configuration.get_configuration()
    access_token = spotify_auth_refresh.refresh_access_token(access["refresh_token"], access["client_id"], access["client_secret"],access["redirect_uri"])
    return access_token

def get_track_ids(access_token):
    reddit_data = reddit.reddit_spotify_data()

    track_ids = []
    for post in reddit_data:
        if(post["type"] == "track"):
            track_ids.append(post["id"])
        elif (post["type"] == "album"):
            album_tracks = spotify.get_track_ids_from_album(post["id"], access_token)
            track_ids = track_ids + album_tracks
    return track_ids