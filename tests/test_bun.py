import allure
import pytest
from praktikum.bun import Bun
from data import Data


class TestBun:
    @pytest.mark.parametrize("name, price", [
        (Data.fluorescent_bun, Data.fluorescent_bun_price),
        (Data.crater_bun, Data.crater_bun_price)
    ])

    @allure.title('Тест на успешную проверку получения имени')
    def test_get_name_successfully(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", [
        (Data.fluorescent_bun, Data.fluorescent_bun_price),
        (Data.crater_bun, Data.crater_bun_price)
    ])
    @allure.title('Тест на успешную проверку получения цены')
    def test_get_price_successfully(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
