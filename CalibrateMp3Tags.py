# calibrate MP3 tags to correct
from mutagen.easyid3 import EasyID3
import sys
import os
import shutil

if len(sys.argv) < 2:
    print('''
    Wrong usage :(
    Right Usage: python3 CalibrateMp3Tags.py mp3_source_path mp3_dest_path
    mp3_source_path: A directory exists containing mp3 files.
    mp3_dest_path: This folder will be automaticly created by this script.
          ''')
path = sys.argv[1]
dest = sys.argv[2]
files = os.listdir(path)
shutil.copytree(path, dest)
for file in files:
    audio = EasyID3(dest + os.sep + file)
    print("Before processing:")
    print(audio)
    audio['artist'] = '曹方'
    audio['title'] = file[:-4]
    audio['album'] = '黑色香水'
    audio.save()
    print("After processing:")
    print(audio)

