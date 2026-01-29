import pytest
from bun import Bun

class TestBun:
    # в методах класса Bun не реализовано отсечение по типу, поэтому тесты проходят с любыми параметрами
    @pytest.mark.parametrize(
        'name, price',
        [
            ('Sweet_Bun', 15),
            ('', 15),
            (None, 15),
            (15, 15)
        ]
    )
    def test_get_name_is_success(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name


    # в методах класса Bun не реализовано отсечение по типу, поэтому тесты проходят с любыми параметрами
    @pytest.mark.parametrize(
        'name, price',
        [
            ('Sweet_Bun', 15),
            ('Sweet_Bun', -15),
            ('Sweet_Bun', '15'),
            ('Sweet_Bun', 15.25)
        ]
    )
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price

    def test_change_name(self):
        bun = Bun('sweet', 0.5)
        bun.name = 'salt'
        assert bun.get_name() == 'salt'

    def test_change_price(self):
        bun = Bun('sweet', 0.5)
        bun.price = 60
        assert bun.get_price() == 60
