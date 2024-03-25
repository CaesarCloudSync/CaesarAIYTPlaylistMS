import re
import sys
from pytube import Playlist

class CaesarAIYoutube:
    @staticmethod
    def get_playlist_videos(url):
        playlist = Playlist(url)
        return [video.watch_url for video in playlist.videos]
