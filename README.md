# YouTube Channel Downloader and MP3 Metadata Updater

This Python script allows you to download all playlists from a specified YouTube channel and add metadata (such as artist name, album name, and bitrate) to the downloaded MP3 files. The script utilizes multi-threading to download videos and update metadata concurrently, significantly speeding up the process for large collections of content.

## Features
- **Download YouTube playlists**: The script downloads the audio files from all playlists of a given YouTube channel.
- **OAuth authentication**: It authenticates the user using OAuth and caches credentials for future use.
- **MP3 metadata update**: After downloading, the script adds metadata (artist, album name, and bitrate) to the audio files.
- **Multi-threading**: Uses `ThreadPoolExecutor` to download and process multiple files in parallel.
- **Filename sanitization**: Handles and sanitizes playlist and song names that contain special characters (such as `/`, `\`, `|`, etc.).

## Requirements

Before running the script, you will need to install the following dependencies:

- `pytubefix`: For accessing YouTube channels and downloading content.
- `pyDub`: For handling the transcoding of files.
- `mutagen`: For updating MP3 metadata.
- Python 3.x and the standard libraries: `os`, `sys`, `re`, `concurrent.futures`.

You can install the required Python packages using `pip`:

```bash
pip install pytubefix pydub mutagen
```

## Usage

```bash
python main.py <YouTube_Channel_URL>
```
