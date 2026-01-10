import pytest

from Diplom_1.praktikum.bun import Bun
from Diplom_1.data import BUN_DATA

class TestBun:
    @pytest.mark.parametrize('name', ['Классическая булочка', '', 'Длинное имя фэнси булочки для хипстеров органик и лалалала'])
    def test_get_name(self, name):
        bun = Bun(name, BUN_DATA.get('price'))
        assert bun.get_name() == name

    @pytest.mark.parametrize('price', [25, 0, 1000000, 99.99])
    def test_get_price(self, price):
        bun = Bun(BUN_DATA.get('name'), price)
        assert bun.get_price() == price