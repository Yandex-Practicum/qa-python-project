import pytest
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize('name,price', [
        ('black bun', 100),
        ('white bun', 200),
        ('red bun', 300)
    ])
    def test_bun_initialization(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    @pytest.mark.parametrize('name,price,expected_name', [
        ('black bun', 100, 'black bun'),
        ('white bun', 200, 'white bun'),
        ('red bun', 300, 'red bun')
    ])
    def test_get_name(self, name, price, expected_name):
        bun = Bun(name, price)
        assert bun.get_name() == expected_name

    @pytest.mark.parametrize('name,price,expected_price', [
        ('black bun', 100, 100),
        ('white bun', 200, 200),
        ('red bun', 300, 300)
    ])
    def test_get_price(self, name, price, expected_price):
        bun = Bun(name, price)
        assert bun.get_price() == expected_price
