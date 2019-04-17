# -*- coding: utf-8 -*-

import requests

fake_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",  # noqa
    "Accept-Charset": "UTF-8,*;q=0.5",
    "Accept-Encoding": "gzip,deflate,sdch",
    "Accept-Language": "en-US,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0",  # noqa
    "referer": "https://www.google.com",
}

def get_detail(song_id):
    params = {
        "v": "2.0",
        "app_key": "1",
        "r": "song/detail",
        "id": song_id,
    }
    s = requests.Session()
    s.headers.update(fake_headers)
    # 获取cookie
    s.head("http://m.xiami.com")
    s.headers.update({"referer": "http://m.xiami.com/"})

    r = s.get("http://api.xiami.com/web", params=params)
    if r.status_code != requests.codes.ok:
        raise Exception("获取音乐失败")
    j = r.json()
    print("singer:{}\nimg:{}\ntitle:{}\nlyric:{}\naudio:{}".format(
        j["data"]["song"]["singers"],
        j["data"]["song"]["logo"],
        j["data"]["song"]["song_name"],
        j["data"]["song"]["lyric"],
        j["data"]["song"]["listen_file"],
    ))


get_detail("1808595482")
