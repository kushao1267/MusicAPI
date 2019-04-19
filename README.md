# MusicAPI
![GitHub](https://img.shields.io/github/license/kushao1267/MusicAPI.svg)

## About
提供了国内许多音乐的API，支持通过music_id和分享链接两种方式来获取歌曲信息及下载链接（版权、会员的除外）。
使用者可以很容易地添加其他音乐类的API。

目前已支持的音乐有:
- [x] 网易云音乐
- [x] QQ音乐
- [x] 虾米音乐

注: 该仓库仅可用于学习和交流实验用途，若用于商业用途，与本人无关。

## Install

## Usage

1.使用music_id访问

```
$ python -m mozart -n netease -l http://music.163.com/song/1358275974/\?userid\=1769873017
[Music]
singer:李子璇
song:豆你玩
cover:http://p1.music.126.net/326BBneDl4izrTBF8vJJxA==/109951163993105848.jpg
download_url:http://m10.music.126.net/20190419145523/620fa37967fa54ab80c9987dbaba8e4a/ymusic/045d/0e5d/0553/37a1dc7beb972befb40629f085a5eb39.mp3
```

2.使用music share url访问

```
$ python -m mozart -n netease -m 1358275974
[Music]
singer:李子璇
song:豆你玩
cover:http://p2.music.126.net/326BBneDl4izrTBF8vJJxA==/109951163993105848.jpg
download_url:http://m10.music.126.net/20190419145641/41f171066b22d8e496b63ff67c6ca429/ymusic/045d/0e5d/0553/37a1dc7beb972befb40629f085a5eb39.mp3
```
## License
[MIT License](https://github.com/kushao1267/facade/blob/master/LICENSE)