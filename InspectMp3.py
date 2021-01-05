import sys
from mutagen.easyid3 import EasyID3
import chardet

if len(sys.argv) < 2:
    print('''
    Wrong usage :(
    Right Usage: python3 InspectMp3.py mp3_source_path
          ''')
audio = EasyID3(sys.argv[1])
print(type(audio['album'][0]))
print(audio['album'][0].encode('utf-8'))
print(chardet.detect(str.encode(audio['album'][0])))
print(audio)
