# ⏯️ YouTube Channel Feed Downloader

This Python script allows you to download videos from YouTube channels using their RSS feeds. By providing a list of channel URLs with their corresponding channel IDs, the script fetches the latest videos from each channel and downloads them using the yt-dlp command-line tool.

### Requirements

- Python 3.x
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)

## Setup

1. Clone or download the repository to your local machine

`git clone git@github.com:Kaya-Sem/local_youtube.git`

2. Install the required packages:

`pip install -r requirements.txt`

3. Install **yt-dlp**:

`pip install yt-dlp`

## Usage

1. Create a text file containing a list of URLs, each representing a YouTube channel feed. Each URL should be on a separate line and should include the channel ID appended to the base URL.

```
https://www.youtube.com/feeds/videos.xml?channel_id=
```

For example:

```
https://www.youtube.com/feeds/videos.xml?channel_id=UCV9s_u7uoGoEKFRjiRp8p2Q
https://www.youtube.com/feeds/videos.xml?channel_id=UClHVl2N3jPEbkNJVx-ItQIQ
```

2. Run the script and provide the path to the text file as a command-line argument:

```
python main.py path/to/url_file.txt
```

This will fetch the latest videos from each channel in the URL file and download them using `yt-dlp`
