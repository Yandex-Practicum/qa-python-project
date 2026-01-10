from praktikum.bun import Bun


def test_get_name():
    burger = Bun('Rufl', 70)
    name = burger.get_name()
    assert 'Rufl' == name


def test_get_price():
    burger = Bun('Rufl', 70)
    price = burger.get_price()
    assert 70 == price
