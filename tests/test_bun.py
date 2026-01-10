import allure
import pytest
from praktikum.bun import Bun

class TestBun:

    @allure.title('Проверка названия')
    @pytest.mark.parametrize('name', [
    'burger_1',
    'burger_2',
    'burger_3'
])
    def test_bun_get_name(self, name):
        bun = Bun(name, price=100)
        assert bun.get_name() == name


    @allure.title('Проверка цены')
    @pytest.mark.parametrize('price', [
    100,
    200,
    300
])
    def test_bun_get_price(self, price):
        bun = Bun(name='burger', price=price)
        assert bun.get_price() == price
