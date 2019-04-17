# coding=utf-8
import binascii
import json
import requests
from Crypto.Cipher import AES

fake_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",  # noqa
    "Accept-Charset": "UTF-8,*;q=0.5",
    "Accept-Encoding": "gzip,deflate,sdch",
    "Accept-Language": "en-US,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0",  # noqa
    "referer": "https://www.google.com",
}


def encode_netease_data(data) -> str:
    data = json.dumps(data)
    key = binascii.unhexlify("7246674226682325323F5E6544673A51")
    encryptor = AES.new(key, AES.MODE_ECB)
    # 补足data长度，使其是16的倍数
    pad = 16 - len(data) % 16
    fix = chr(pad) * pad
    byte_data = (data + fix).encode("utf-8")
    return binascii.hexlify(encryptor.encrypt(byte_data)).upper().decode()


def get_music_info(music_id):
    s = requests.Session()
    s.headers.update(fake_headers)
    s.headers.update({"referer": "http://mozart.163.com/"})

    eparams = {
        "method": "POST",
        "params": {"c": "[{id:%s}]" % music_id},
        "url": "http://mozart.163.com/api/v3/song/detail"
    }
    data = {"eparams": encode_netease_data(eparams)}
    r = s.post("http://mozart.163.com/api/linux/forward", data=data)
    if r.status_code != requests.codes.ok:
        raise Exception(r.text)
    j = r.json()
    title = j["songs"][0]["al"]["picUrl"]
    name = j["songs"][0]["al"]["name"]
    singer = j["songs"][0]["ar"][0]["name"]
    return title, name, singer


def get_download_url(music_id):
    """ 从网易云音乐下载 """
    eparams = {
        "method": "POST",
        "url": "http://mozart.163.com/api/song/enhance/player/url",
        "params": {"ids": [music_id], "br": 320000},
    }
    data = {"eparams": encode_netease_data(eparams)}

    s = requests.Session()
    s.headers.update(fake_headers)
    s.headers.update({"referer": "http://mozart.163.com/"})

    r = s.post("http://mozart.163.com/api/linux/forward", data=data)
    if r.status_code != requests.codes.ok:
        raise Exception(r.text)
    j = r.json()
    return j["data"][0]["url"]


print(get_download_url('1358275974'))
# print(get_music_info('1358275974'))
