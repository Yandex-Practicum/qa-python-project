import pytest
from praktikum.bun import Bun

class TestBun:

    @pytest.mark.parametrize('name,price', [
        ('pudge bun', 100),
        ('te4ka bun', 200)
    ])
    def test_get_name(self, name, price):
        bun = Bun(name,price)
        assert bun.get_name() == name

    def test_get_price(self, bun):
        assert bun.get_price() == 100
