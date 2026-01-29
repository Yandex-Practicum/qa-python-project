import allure
import pytest

import data
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize('name, price', data.bun_data.items())
    @allure.title('проверка инициализации булки для бургера. Имя и цена')
    def test_bun_creation(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    @pytest.mark.parametrize('name, price', data.bun_data.items())
    @allure.title('Проверка метода get_name')
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', data.bun_data.items())
    @allure.title('Проверка метода get_price')
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
