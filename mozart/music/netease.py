import binascii
import json
import requests
from Crypto.Cipher import AES
from . import Music
import config


def encode_netease_data(data) -> str:
    data = json.dumps(data)
    key = binascii.unhexlify("7246674226682325323F5E6544673A51")
    encryptor = AES.new(key, AES.MODE_ECB)
    # 补足data长度，使其是16的倍数
    pad = 16 - len(data) % 16
    fix = chr(pad) * pad
    byte_data = (data + fix).encode("utf-8")
    return binascii.hexlify(encryptor.encrypt(byte_data)).upper().decode()


class Netease(Music):
    def __init__(self, *args, **kwargs):
        super(Netease, self).__init__(*args, **kwargs)
        # 网易音乐的初始化
        self.music_id = self.get_music_id_from_url(self.real_url)
        self._get_music_info(self.music_id)
        self._get_download_url(self.music_id)

    def _get_music_info(self):
        s = requests.Session()
        s.headers.update(config.fake_headers)
        s.headers.update({"referer": "http://music.163.com/"})

        eparams = {
            "method": "POST",
            "params": {"c": "[{id:%s}]" % self.music_id},
            "url": "http://music.163.com/api/v3/song/detail"
        }
        data = {"eparams": encode_netease_data(eparams)}
        r = s.post("http://music.163.com/api/linux/forward", data=data)
        if r.status_code != requests.codes.ok:
            raise Exception(r.text)
        j = r.json()
        self._cover = j["songs"][0]["al"]["picUrl"]
        self._song = j["songs"][0]["al"]["name"]
        self._singer = j["songs"][0]["ar"][0]["name"]

    def _get_download_url(self):
        """ 从网易云音乐下载 """
        eparams = {
            "method": "POST",
            "url": "http://music.163.com/api/song/enhance/player/url",
            "params": {"ids": [self.music_id], "br": 320000},
        }
        data = {"eparams": encode_netease_data(eparams)}

        s = requests.Session()
        s.headers.update(config.fake_headers)
        s.headers.update({"referer": "http://music.163.com/"})

        r = s.post("http://music.163.com/api/linux/forward", data=data)
        if r.status_code != requests.codes.ok:
            raise Exception(r.text)
        j = r.json()
        self._download_url = j["data"][0]["url"]

    @classmethod
    def get_music_id_from_url(cls, url):
        return url

# print(get_music_info('1358275974'))
