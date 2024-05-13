import argparse
import feedparser
import subprocess

# Author: Kaya-Sem
#
#
# simple script that can read a youtube creator's rss and downloads their most recent videos

DEFAULT_AMOUNT_VIDS = 2
DEFAULT_URLS_PATH = "template_urls.txt"

# TODO create template shell command that people can implement and override themselves
# TODO  download location
# TODO allow comments in urls file


def download_video(url):
    subprocess.run(["yt-dlp", url])

def parseURLfile(path):
    with open(path) as file:
        lines = [line.strip() for line in file if line.strip() and not line.strip().startswith("//")]

    return lines

def main(filepath, num_videos=None):

    if filepath is None:
        filepath = DEFAULT_URLS_PATH

    if num_videos is None:
        num_videos = DEFAULT_AMOUNT_VIDS

    urls = parseURLfile(filepath)
    num_downloaded = 0

    for index, item in enumerate(urls):
        print(f"parsing url {index + 1}: {item}\n")
        feed = feedparser.parse(item)
    
        for entry in feed.entries:
            url = entry.link
        
            if "youtube.com" in url or "youtu.be" in url:
                download_video(url)
                num_downloaded += 1
                if num_downloaded >= num_videos:
                    return  # Stop when the desired number of videos have been downloaded

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download videos from YouTube RSS feeds.")
    parser.add_argument("-urls", help="Path to the file containing URLs.")
    parser.add_argument("--num-videos", type=int, help="Number of latest videos to download.")

    args = parser.parse_args()

    main(args.urls, args.num_videos)

