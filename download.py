import requests
import json

def downloader(url):
    print(url)
    raw = requests.get(url)
    