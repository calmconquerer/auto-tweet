import requests

base_url = "https://api.medium.com/v1"


res = requests.get(
    "https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@wasiullah-khan21"
)
