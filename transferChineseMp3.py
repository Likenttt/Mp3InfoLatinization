import os
import shutil
import sys
from mutagen.easyid3 import EasyID3
from pypinyin import lazy_pinyin
from sys import exit


def batchTransfer(path, dest):
    # Get all file names in folder. Variable files is Like ['透明对白.mp3','稻草人.mp3']
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(path, dest)
    files = os.listdir(dest)
    for file in files:
        transfer(file, dest)


def transfer(file, dest):
    suffix = file[-4:]
    if suffix != ".mp3":
        print("Not valid mp3 format～")
        exit(1)
    filename = file[:-4]
    print("Current file:" + filename)
    audio = EasyID3(dest + os.sep + file)
    print(audio)
    # Notice： audio['title'] is a list
    title = audio['title'][0]
    artist = audio['artist'][0]
    album = audio['album'][0]
    if title is not None and title != '' and containsCHNCharacters(title):
        title_array = lazy_pinyin(title)
        # 别来无恙 -> Bie Lai Wu Yang -> Bie Lai Wu Yang
        audio['title'] = ' '.join(title_array).title().replace(" ", "")
        print("audio['title']:" + title)
    if artist is not None and artist != '' and containsCHNCharacters(artist):
        artist_array = lazy_pinyin(artist)
        audio['artist'] = ' '.join(artist_array).title().replace(" ", "")
    if album is not None and album != '' and containsCHNCharacters(album):
        album_array = lazy_pinyin(album)
        audio['album'] = ' '.join(album_array).title().replace(" ", "")
    audio.save()
    if filename is not None and filename != '' and containsCHNCharacters(filename):
        file_array = lazy_pinyin(filename)
        new_file = ' '.join(file_array).title().replace(" ", "")
        os.rename(dest + os.sep + file, dest + os.sep + new_file + suffix)


def containsCHNCharacters(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


if len(sys.argv) < 3:
    print("Invalid parameter array~ parameters insufficient")
    exit(1)
path = sys.argv[1]
dest = sys.argv[2]
print(sys.argv)
if os.path.isdir(path):
    print("Batch～")
    batchTransfer(path, dest)
elif os.path.isfile(path):
    print("Single file～")
    # 获取文件名
    file = os.path.basename(path)
    shutil.copyfile(path, dest + os.sep + file)
    transfer(file, dest)
else:
    print("路径非法")
    exit(1)
