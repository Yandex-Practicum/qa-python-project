from praktikum.bun import Bun


def test_get_name_returns_bun_name():
    bun = Bun('black bun', 100)

    assert bun.get_name() == 'black bun'


def test_get_price_returns_bun_price():
    bun = Bun('black bun', 100)

    assert bun.get_price() == 100