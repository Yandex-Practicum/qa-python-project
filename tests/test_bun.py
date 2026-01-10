import pytest
from praktikum.bun import Bun


class TestBun:

    def test_get_name_added_name_returned(self):
        bun = Bun('custom name', 150)
        assert bun.get_name() == 'custom name'

    def test_name_type_is_str(self):
        bun = Bun('custom name', 150)
        assert isinstance(bun.get_name(), str)

    @pytest.mark.parametrize('name,price', [
        ('bun one', 150),
        ('bun two', 55.95),
        ('bun three', 0)
    ])
    def test_get_price_added_price_returned(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price

    @pytest.mark.parametrize('name,price', [
        ('bun one', 150),
        ('bun two', 55.95),
        ('bun three', 0)
    ])
    def test_price_type_is_number(self, name, price):
        bun = Bun(name, price)
        assert isinstance(bun.get_price(), (int, float))
