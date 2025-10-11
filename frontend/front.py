import requests

print("Enter video URL...")
url = input()

# Does a simple HTTP code check
def checkurl(link):
    load = requests.get(link)
    if load.status_code == 200:
        print("Video loaded fine, moving on.")
        return 200
    elif load.status_code == 404:
        print("Page not found. Are you sure you inputted the url correctly?")
        return 404
    elif load.status_code == 403:
        print("Forbidden. Are you sure you inputted the url correctly?")
        return 403
    elif load.status_code == 500:
        print("Server error. Check your internet or youtube's status")
        return 500

# Makes sure the video is not removed or anything    
def videocheck(url):
    code = checkurl(url)
    if code==200:
        video = requests.get(url)
        content = video.text
        if url in content:
            print("Video is up and working, downloading..")
            # Add call to downloader function here
        else:
            print("Video not found")

videocheck(url)


