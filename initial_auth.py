import requests
import json
import spotify_configuration

access = spotify_configuration.get_configuration()

client_id = access["client_id"]
client_secret = access["client_secret"]
redirect_uri = access["redirect_uri"]
scope = "playlist-modify-public, playlist-modify-private"

auth_code = access["auth_code"]

app_request_url = "https://accounts.spotify.com/api/token"
bodyparams = {"grant_type":"authorization_code", "code":auth_code, "redirect_uri":redirect_uri}
response = requests.post(app_request_url, data = bodyparams, auth = (client_id, client_secret))

print(response.text)
