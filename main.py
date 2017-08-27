import reddit
import spotify
import configparser

def main():
    access_token = get_access_token()
    track_ids = get_track_ids()
    spotify.add_tracks_to_playlist(track_ids, access_token)

def get_access_token():
    config = configparser.ConfigParser()
    config.read("C:\\Users\\Savvas\\RHardstyleSpotifyAccess.ini")
    access = config["RHARDSTYLESPOTIFY_ACCESS"]
    access_token = access["access_token"]
    return access_token

def get_track_ids():
    reddit_data = reddit.reddit_spotify_data()

    track_ids = []
    for post in reddit_data:
        if(post["type"] == "track"):
            track_ids.append(post["id"])
    return track_ids

main()
