import feedparser
import subprocess

RSS_FEED_URL = "https://www.youtube.com/feeds/videos.xml?channel_id=UCaiVt4r6YLPzJVgr7pOmD6w"

def download_video(url):
    subprocess.Popen(["yt-dlp", url])

def main():
    feed = feedparser.parse(RSS_FEED_URL)
    
    for entry in feed.entries:
        url = entry.link
        
        if "youtube.com" in url or "youtu.be" in url:
            download_video(url)

if __name__ == "__main__":
    main()
