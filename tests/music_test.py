import pytest
from mozart.music import music_map, Netease, QQ, XiaMi


def test_music_name():
    music_platforms = music_map.keys()
    assert 'qq' in music_platforms
    assert 'netease' in music_platforms
    assert 'xiami' in music_platforms


def test_QQ_music_id_method():
    result = QQ(music_id="001TXSYu1Gwuwv", use_id=True).__repr__()
    assert "薛之谦" in result
    assert "刚刚好" in result
    assert "stream.qqmusic.qq.com" in result


def test_Netease_music_id_method():
    result = Netease(music_id="1358275974", use_id=True).__repr__()
    assert "李子璇" in result
    assert "豆你玩" in result
    assert "" in result


def test_XiaMi_music_id_method():
    result = XiaMi(music_id="1459299", use_id=True).__repr__()
    assert "Jo Dee Messina" in result
    assert "I Know a Heartache When I See One" in result
    assert "" in result  # domain


def test_QQ_music_link_method():
    result = QQ(url="http://url.cn/5B0gwrl", use_id=False).__repr__()
    assert "薛之谦" in result
    assert "刚刚好" in result
    assert "stream.qqmusic.qq.com" in result


def test_Netease_music_link_method():
    result = Netease(url="http://music.163.com/song/1358275974/?userid=1769873017", use_id=False).__repr__()
    assert "李子璇" in result
    assert "豆你玩" in result
    assert "" in result


def test_XiaMi_music_link_method():
    result = XiaMi(url="https://www.xiami.com/song/1459299", use_id=False).__repr__()
    assert "Jo Dee Messina" in result
    assert "I Know a Heartache When I See One" in result
    assert "" in result  # domain
