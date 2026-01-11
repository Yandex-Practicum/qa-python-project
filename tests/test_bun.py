from praktikum.bun import Bun


def test_bun_get_name():
    assert Bun('test_bun', 3).get_name() == 'test_bun'

def test_bun_get_price():
    assert Bun('test_bun', 3).get_price() == 3