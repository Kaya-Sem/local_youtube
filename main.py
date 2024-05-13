
import argparse
import feedparser
import subprocess

DEFAULT_AMOUNT_VIDS = 2
DEFAULT_URLS_PATH = "template_urls.txt"

def download_video(url):
    subprocess.run(["yt-dlp", url])

def parseURLfile(path):
    with open(path) as file:
        lines = [line.strip() for line in file if line.strip() and not line.strip().startswith("//")]
    return lines

def main(filepath, num_videos):
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
                    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download videos from YouTube RSS feeds.")
    parser.add_argument("-urls", help="Path to the file containing URLs.")
    parser.add_argument("--num-videos", type=int, help="Number of latest videos to download.")

    args = parser.parse_args()

    urls_path = args.urls if args.urls is not None else DEFAULT_URLS_PATH
    num_videos = args.num_videos if args.num_videos is not None else DEFAULT_AMOUNT_VIDS

    main(urls_path, num_videos)

