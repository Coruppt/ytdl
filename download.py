import requests
import json

def jsoncirc(html):
    marker = "ytInitialPlayerResponse"
    start = html.find(marker)
    if start == -1:
        return None
    start = html.find("{",start)
    count = 0
    for i in range(start, len(html)):
        if html[i]=="{":
            count +=1
        elif html[i] == "}":
            count -= 1
            if count == 0:
                end = i + 1
                break
    else:
        return None

    json_str = html[start:end]
    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        # youtube sometimes uses \u0026 etc
        json_str = json_str.encode("utf-8").decode("unicode_escape")
        return json.loads(json_str)


def downloader(url):
    print(f"Downloading... {url}")
    raw = requests.get(url)
    html = raw.text
    core = jsoncirc(html)
    streaming = core.get("streamingData", {})
    for fmt in streaming.get("formats", []):
        print(fmt["url"])


    