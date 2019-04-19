from .__version__ import __version__
import logging
from mozart.music import get_music_handler, music_map
# http://url.cn/5B0gwrl
# https://www.xiami.com/song/1459299
# http://music.163.com/song/1358275974/?userid=1769873017


def cli():
    """
    command line program
    """
    import argparse

    def get_args():
        """
        Parse programs arguments
        """
        parser = argparse.ArgumentParser(
            description="mozart - ♪ Nice API for developers who like musics",
            usage="python -m mozart [-h] [-v] [-l LINK] [-n NAME] [-m MUSIC_ID]"
        )

        parser.add_argument(
            "-v", "--version", action="version",
            version='%(prog)s - version {}'.format(__version__))
        parser.add_argument(
            "-l", "--link", dest='link', type=str, default="",
            help='print out all info about this music from link.')
        parser.add_argument(
            "-n", "--name", dest='name', type=str, default="",
            help='name of music site. avaliable are: {}'.format(', '.join(music_map.keys())))
        parser.add_argument(
            "-m", "--music", dest='music_id', type=str, default="",
            help='print out all info about this music from music id.')
        args = parser.parse_args()
        if not args.name or (not args.link and not args.music_id):
            parser.print_help()
            exit(0)
        return args

    args = get_args()
    # init logger
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)-8s | %(name)s: %(msg)s ",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logger = logging.getLogger("mozart")

    # main proccess
    if args.music_id and args.music_id.isdigit() and args.name in ["qq", "xiami", "netease"]:
        logger.debug("use music id to request")
        got, handler = get_music_handler(args.name)
        if got:
            handler(music_id=args.music_id, use_id=True)

    elif args.link:
        logger.debug("use link to request")
        got, handler = get_music_handler(args.name)
        if got:
            handler(url=args.link, use_id=False)
    else:
        exit(-1)
