import pytest
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize("name, price", [
        ('Булочка от Практикума', 100),
        ('Булочка Дипломная', 200),
    ])
    def test_bun_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", [
        ('Булочка от Практикума', 100),
        ('Булочка Дипломная', 200),
    ])
    def test_bun_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
