import os
import shutil
import sys
from mutagen.easyid3 import EasyID3
from pypinyin import lazy_pinyin
from sys import exit


def batchTransfer(path,dest):
    #文件名列表而已
    files = os.listdir(dest)
    shutil.copytree(path,dest)
    for file in files:
        transfer(file,dest)

def transfer(file,dest):
    tp = file[-3:]
    if tp != "mp3":
        print("文件不是一个有效的mp3文件～")
        exit(1)
    filename = file[:-4]
    print("当前处理的文件"+filename)
    # os.rename(file, "tst.mp3")
    #audio = eyed3.load(path+"\\"+file)
    audio = EasyID3(dest + os.sep+ file)
    if audio['title'] is not None and audio['title'] !='' and containsCHNCharacters(audio['title']):
        title_array = lazy_pinyin(audio['title'])
        # 别来无恙 -> Bie Lai Wu Yang -> Bie Lai Wu Yang
        audio['title'] = ' '.join(title_array).title().replace(" ", "")
    if audio['artist'] is not None and audio['artist'] !='' and containsCHNCharacters(audio['artist']):
        artist_array = lazy_pinyin(audio['artist'])
        audio['artist'] = ' '.join(artist_array).title().replace(" ", "")
    if audio['album'] is not None and audio['album'] !='' and containsCHNCharacters(audio['album']):
        album_array = lazy_pinyin(audio['album'])
        audio['album'] = ' '.join(album_array).title().replace(" ", "")
    audio.save()
    if file is not None and file !='' and containsCHNCharacters(file):
        file_array = lazy_pinyin(file)
        new_file = ' '.join(file_array).title().replace(" ", "")
        os.rename(dest + os.sep+ file,dest + os.sep+new_file)


def containsCHNCharacters(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

# 接收一个路径参数然后将mp3的信息修改后写回
if len(sys.argv) < 3:
  print("参数长度非法")
  exit(1)
path = sys.argv[1]
dest = sys.argv[2]
print(sys.argv)
if not os.path.isdir(dest):
    print("目标路径必须是一个文件夹～")
    exit(1)

if os.path.isdir(path):
    print("批量文件转换～")
    batchTransfer(path,dest)
elif os.path.isfile(path):
    print("单个文件转换～")
    #获取文件名
    file = os.path.basename(path)
    shutil.copyfile(path,dest+os.sep+file)
    transfer(file,dest)
else:
    print("路径非法")
    exit(1)
