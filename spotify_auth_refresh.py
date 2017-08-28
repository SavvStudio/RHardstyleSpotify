import requests
import json
def refresh_access_token(refresh_token, client_id, client_secret, redirect_uri):
    response = requests.post("https://accounts.spotify.com/api/token", data = {"grant_type":"refresh_token", "refresh_token":refresh_token, "redirect_uri":redirect_uri}, auth=(client_id,client_secret))
    return json.loads(response.text)["access_token"]