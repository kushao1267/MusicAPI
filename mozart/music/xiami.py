# -*- coding: utf-8 -*-
from . import Music
import config
import requests


class XiaMi(Music):
    def __init__(self, *args, **kwargs):
        super(XiaMi, self).__init__(*args, **kwargs)
        # 虾米音乐的初始化
        self.music_id = self.get_music_id_from_url(self.real_url)

        params = {
            "v": "2.0",
            "app_key": "1",
            "r": "song/detail",
            "id": self.music_id,
        }
        s = requests.Session()
        s.headers.update(config.fake_headers)
        # 获取cookie
        s.head("http://m.xiami.com")
        s.headers.update({"referer": "http://m.xiami.com/"})

        r = s.get("http://api.xiami.com/web", params=params)
        if r.status_code != requests.codes.ok:
            raise Exception("获取音乐失败")
        j = r.json()
        self._song = j["data"]["song"]["song_name"]
        self._singer = j["data"]["song"]["singers"]
        self._cover = j["data"]["song"]["logo"]
        self._download_url = j["data"]["song"]["listen_file"]
        # j["data"]["song"]["lyric"]  # 歌词

    def _get_music_info(self):
        pass

    def _get_download_url(self):
        pass

    @classmethod
    def get_music_id_from_url(cls, url):
        return url

# XiaMi("1808595482")
