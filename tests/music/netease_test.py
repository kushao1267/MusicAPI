from mozart.music import Netease
from tests.music.helpers import assert_music


def test_a2u_provider():
    assert_music(Netease())