# coding=utf-8
import random
import requests

fake_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",  # noqa
    "Accept-Charset": "UTF-8,*;q=0.5",
    "Accept-Encoding": "gzip,deflate,sdch",
    "Accept-Language": "en-US,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0",  # noqa
    "referer": "https://www.google.com",
}

wget_header = {
    "Accept": "*/*",
    "Accept-Encoding": "identity",
    "User-Agent": "Wget/1.19.5 (darwin17.5.0)",
}

ios_ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46"
" (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"


def get_guid():
    return str(random.randrange(1000000000, 10000000000))


def operate_vkey(guid):
    """计算vkey"""
    params = {"guid": guid, "format": "json", "json": 3}
    s = requests.Session()
    s.headers.update(fake_headers)
    s.headers.update(
        {"referer": "http://y.qq.com", "User-Agent": ios_ua}
    )

    r = s.get("http://base.music.qq.com/fcgi-bin/fcg_musicexpress.fcg", params=params)
    if r.status_code != requests.codes.ok:
        raise Exception(r.text)
    j = r.json()
    if j["code"] != 0:
        raise Exception(r.text)

    return j["key"]


def construct_download_url(mid):
    guid = get_guid()
    vkey = operate_vkey(guid)
    # title, singer = get_music_info(mid) // 有些歌曲获取title和singer会失败
    rate = 128
    for prefix in ["M800", "M500", "C400"]:
        url = "http://dl.stream.qqmusic.qq.com/%s%s.mp3?vkey=%s&guid=%s&fromtag=1" % (
            prefix,
            mid,
            vkey,
            guid,
        )

        try:
            r = requests.get(
                url,
                stream=True,
                headers=wget_header,
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
    print(url)


def get_music_info(mid):
    url = 'https://u.y.qq.com/cgi-bin/musicu.fcg'
    params = {
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'data': '%7b%22songinfo%22%3a%7b%22method%22%3a%22get_song_detail_yqq%22%2c%22'
                'param%22%3a%7b%22song_type%22%3a0%2c%22song_mid%22%3a%22{}%22%7d%2c%22'
                'module%22%3a%22music.pf_song_detail_svr%22%7d%7d'.format(mid),
    }
    resp = requests.get(url, params=params)
    data = resp.json()["songinfo"]["data"]["track_info"]
    title = data["name"]
    singer = data["singer"][0]["name"]
    return title, singer


construct_download_url("001luHbo2nQT1Y")
