from mozart.cli import main


def test_cli_main():
    ret = main(['-n', 'qq', '-l', 'http://url.cn/5B0gwrl'])

    assert 0 == ret
