from pytube import YouTube, streams, Search
from validator_collection import checkers
import sys

queue = dict()
currentMusicId = 1
DOWNLOAD_PATH = str(sys.argv[1])  # get download path from terminal run command
BASE_YOUTUBE_URL = 'https://www.youtube.com/watch?v='


def download_music(url):
    try:
        video = YouTube(url)
        stream = video.streams.filter(type='audio').last()
        stream.download(output_path=DOWNLOAD_PATH)
        print('download complete...')
        return video.title
    except:
        print('can\'t find any video with this url...')


def search_music(user_input):
    search = Search(user_input)
    video = []
    for videos in range(0, 10):
        url = BASE_YOUTUBE_URL + search.results[videos].video_id
        video.append(YouTube(url).title)
    for v in range(0, len(video)):
        print(v+1, ' - ', video[v])
    # ask user to select one of the first 10 youtube response
    user_select = int(input('Which video would you like to download?: ')) - 1
    video_url = BASE_YOUTUBE_URL + search.results[user_select].video_id
    return video_url


def add_music(music_input):
    global currentMusicId
    if checkers.is_url(music_input):
        music_url = music_input
    else:
        music_url = search_music(music_input)

    download_music(music_url)
    currentMusicId += 1



if __name__ == "__main__":
    add_music(' '.join(sys.argv[2:]))

    