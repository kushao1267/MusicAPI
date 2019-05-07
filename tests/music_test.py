import pytest
import re
from mozart.music import music_map, Netease, QQ, XiaMi


def test_music_name():
    music_platforms = music_map.keys()
    assert 'qq' in music_platforms
    assert 'netease' in music_platforms
    assert 'xiami' in music_platforms


def test_qq_music_id():
    result = QQ(music_id="001TXSYu1Gwuwv", use_id=True).__repr__()
    assert "薛之谦" in result
    assert "刚刚好" in result
    assert "stream.qqmusic.qq.com" in result


def test_netease_music_id():
    result = Netease(music_id="1358275974", use_id=True).__repr__()
    assert "李子璇" in result
    assert "豆你玩" in result
    assert "m10.music.126.net" in result


def test_xiami_music_id():
    result = XiaMi(music_id="1459299", use_id=True).__repr__()
    assert "Jo Dee Messina" in result
    assert "I Know a Heartache When I See One" in result
    music_dl = re.findall(r'(http://m\d+.xiami.net)', result)
    assert len(music_dl) > 0  # domain


def test_qq_music_link():
    result = QQ(url="http://url.cn/5B0gwrl", use_id=False).__repr__()
    assert "薛之谦" in result
    assert "刚刚好" in result
    assert "stream.qqmusic.qq.com" in result


def test_netease_music_link():
    result = Netease(url="http://music.163.com/song/1358275974/?userid=1769873017", use_id=False).__repr__()
    assert "李子璇" in result
    assert "豆你玩" in result
    assert "m10.music.126.net" in result


def test_xiami_music_link():
    result = XiaMi(url="https://www.xiami.com/song/1459299", use_id=False).__repr__()
    assert "Jo Dee Messina" in result
    assert "I Know a Heartache When I See One" in result
    music_dl = re.findall(r'(http://m\d+.xiami.net)', result)
    assert len(music_dl) > 0  # domain
