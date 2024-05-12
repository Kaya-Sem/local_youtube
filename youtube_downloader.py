import argparse
import feedparser
import subprocess

def download_video(url):
    subprocess.run(["yt-dlp", url])

def parseURLS(path) :
    with open(path) as file:
        return file.readlines()

def main(filepath):

    urls = parseURLS(filepath)

    for index, item in enumerate(urls):
        print(f"parsing url {index + 1}: {item}\n")
        feed = feedparser.parse(item)
    
        for entry in feed.entries:
           url = entry.link
        
           if "youtube.com" in url or "youtu.be" in url:
               download_video(url)
               break # allow only the last video to be downloaded

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download videos from YouTube RSS feeds.")
    parser.add_argument("filepath", help="Path to the file containing URLs.")

    args = parser.parse_args()

    main(args.filepath)

