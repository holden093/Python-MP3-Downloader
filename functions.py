import re, os, time, random
from pydub import AudioSegment
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TALB, TPE1

def sanitize(name):
    return re.sub(r'[\/:*?"<>|]', '', name)

def download(playlist, channel, root_directory):
    playlist_path = os.path.join(root_directory, channel.channel_name, sanitize(playlist.title))
    if not os.path.exists(playlist_path):
        os.makedirs(playlist_path)
    for video in playlist.videos:
        try:
            audio = video.streams.get_audio_only()
            if audio is not None:
                time.sleep(random.uniform(1, 5))
                audio.download(playlist_path)
            else:
                print(f'No audio for: {video.title} - {video.embed_url}')
        except Exception as e:
            print(f'Errore: {e} in {video.title} - {video.embed_url}')

def update_metadata(song, artist, album, bitrate):
    try:
        mp3_path = f'{os.path.splitext(song)[0]}.mp3'
        AudioSegment.from_file(song).export(mp3_path, format='mp3', bitrate=bitrate)
        if os.path.exists(song):
            os.remove(song)
        audio = MP3(mp3_path, ID3=ID3)                        
        audio.tags.add(TPE1(encoding=3, text=artist))
        audio.tags.add(TALB(encoding=3, text=album))
        audio.tags.add(TIT2(encoding=3, text=os.path.basename(os.path.splitext(song)[0])))                                
        audio.save()
    except Exception as e:
        print(f"Error updating {song}: {e}")