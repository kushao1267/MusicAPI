# coding=utf-8
import random
import requests
from . import Music
import config


def get_guid():
    return str(random.randrange(1000000000, 10000000000))


def operate_vkey(guid):
    """计算vkey"""
    params = {"guid": guid, "format": "json", "json": 3}
    s = requests.Session()
    s.headers.update(config.fake_headers)
    s.headers.update(
        {"referer": "http://y.qq.com", "User-Agent": config.ios_ua}
    )

    r = s.get("http://base.music.qq.com/fcgi-bin/fcg_musicexpress.fcg", params=params)
    if r.status_code != requests.codes.ok:
        raise Exception(r.text)
    j = r.json()
    if j["code"] != 0:
        raise Exception(r.text)

    return j["key"]


class QQ(Music):
    def __init__(self, *args, **kwargs):
        super(QQ, self).__init__(*args, **kwargs)
        # 网易音乐的初始化
        self.music_id = self.get_music_id_from_url(self.real_url)
        self._get_music_info()
        self._get_download_url()

    @classmethod
    def get_music_id_from_url(cls, url):
        return url

    def _get_download_url(self):
        guid = get_guid()
        vkey = operate_vkey(guid)
        # title, singer = get_music_info(mid) // 有些歌曲获取title和singer会失败
        rate = 128
        for prefix in ["M800", "M500", "C400"]:
            url = "http://dl.stream.qqmusic.qq.com/%s%s.mp3?vkey=%s&guid=%s&fromtag=1" % (
                prefix,
                self.music_id,
                vkey,
                guid,
            )

            try:
                r = requests.get(
                    url,
                    stream=True,
                    headers=config.wget_header,
                )
                size = int(r.headers.get("Content-Length", 0))
                # 转换成MB并保留两位小数
                size = round(size / 1048576, 2)
            except:
                pass

            if size > 0:
                if prefix == "M800":
                    rate = 320
                break

        self._download_url = url

    def _get_music_info(self):
        url = 'https://u.y.qq.com/cgi-bin/musicu.fcg'
        params = {
            'format': 'json',
            'inCharset': 'utf8',
            'outCharset': 'utf-8',
            'data': '%7b%22songinfo%22%3a%7b%22method%22%3a%22get_song_detail_yqq%22%2c%22'
                    'param%22%3a%7b%22song_type%22%3a0%2c%22song_mid%22%3a%22{}%22%7d%2c%22'
                    'module%22%3a%22music.pf_song_detail_svr%22%7d%7d'.format(self.music_id),
        }
        resp = requests.get(url, params=params)
        data = resp.json()["songinfo"]["data"]["track_info"]
        self._song = data["name"]
        self._singer = data["singer"][0]["name"]

# construct_download_url("001luHbo2nQT1Y")
