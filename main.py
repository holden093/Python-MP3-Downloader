from pytubefix import Channel
from concurrent.futures import ThreadPoolExecutor
from functions import sanitize, download, update_metadata
import os, sys


def authenticate_channel(channel):
    try:
        first_video = channel.videos[1]
        first_video.streams.get_audio_only().download(filename="auth_test", skip_existing=True)
        print("Authentication successful and credentials cached.")
    except Exception as e:
        print(f'Authentication failed: {e}')
        raise

def main():

    root_directory = os.path.join(os.getcwd(), 'artists')
    bitrate = '192k'
    channel = Channel(sys.argv[1], use_oauth=True, allow_oauth_cache=True)

    print(f'Download {channel.channel_name} cominciato!')
    authenticate_channel(channel)
    channel_path = os.path.join(root_directory, sanitize(channel.channel_name))
    if not os.path.exists(channel_path):
        os.makedirs(channel_path)

    with ThreadPoolExecutor(max_workers=100) as executor:
        for playlist in channel.playlists:
            executor.submit(download, playlist, channel, root_directory)


    if os.path.exists('auth_test'):
        os.remove('auth_test')

    
    print(f'Terminato download {channel.channel_name}')

    with ThreadPoolExecutor(max_workers=100) as executor:
        for album in os.listdir(channel_path):
            album_path = os.path.join(channel_path, album)
            if os.path.isdir(album_path):
                for song in os.listdir(album_path):
                    executor.submit(update_metadata, os.path.join(album_path, song), channel.channel_name, album, bitrate)

    print(f'Aggiunti metadata su tutte le tracce di {channel.channel_name}!')

if __name__ == '__main__':
    main()
