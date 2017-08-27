import urllib.request
import json
import re

reddit_url = lambda site:"https://www.reddit.com/r/hardstyle/search.json?q=flair%3ATrack+site%3A" + site + "&restrict_sr=on&sort=top&t=month"

def reddit_spotify_data():
    url = reddit_url("open.spotify.com")
    data = retrieve_raw_data(url)
    json_data = turn_raw_data_to_json(data)
    children = get_children_from_json_data(json_data)
    urls = get_urls_from_children(children)
    info = extract_info_from_urls(urls)
    return info

def retrieve_raw_data(url):
    return urllib.request.urlopen(url).read()

def turn_raw_data_to_json(raw_data):
    return json.loads(raw_data.decode("utf-8"))

def get_children_from_json_data(json_data):
    return json_data["data"]["children"]

def get_urls_from_children(children):
    urls = []
    for child in children:
        if(child["data"]["score"] > 5):
            urls.append(child["data"]["url"])
    return urls

def extract_info_from_urls(urls):
    info = []
    for url in urls:
        single_url_info = extract_info_from_single_url(url)
        info.append(single_url_info)
    return info

def extract_info_from_single_url(url):
    pattern = re.compile("https://open.spotify.com/(track|album)/([A-Za-z0-9]+)")
    matches = re.findall(pattern, url)
    return {"type": matches[0][0], "id": matches[0][1]}
