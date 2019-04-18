import requests
from mozart import config


class Music(object):
    """
    音乐封装类，实现下载链接，封面图，歌手，歌名的获取
    """

    def __init__(self, url):
        self.real_url = self.get_real_url(url)
        self.music_id = ""
        self._download_url = ""
        self._cover = ""
        self._singer = ""
        self._song = ""
        # 初始化歌曲信息
        pass

    def __repr__(self):
        return "[Music]{singer:%s,song:%s,cover:%s,download_url:%s}" % (
            self._singer, self._song, self._cover, self._download_url)

    @property
    def download_url(self):
        return self._download_url

    @property
    def cover(self):
        return self._cover

    @property
    def singer(self):
        return self._singer

    @property
    def song(self):
        return self._song

    @classmethod
    def get_music_id_from_url(cls, url):
        """
        从real_url获得music id
        """
        raise NotImplementedError("Music's method `get_music_id_from_url` does not implement!")

    @staticmethod
    def get_real_url(url):
        """
        根据分享链接，获取最终访问的URL，支持redirect
        :return: url
        # Now, only qq need redirect
        """
        if 'url.cn' in url:
            r = requests.head(url, allow_redirects=True, headers={"User-Agent": config.ios_ua})
            return r.url
        return url

    def _get_download_url(self):
        raise NotImplementedError("Music's method `_get_download_url` does not implement!")

    def _get_music_info(self):
        raise NotImplementedError("Music's method `_get_music_info` does not implement!")
