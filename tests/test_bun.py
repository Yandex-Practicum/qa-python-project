import pytest
import allure

from conftest import create_bun
from data import Data

@allure.suite('Тесты класса "bun"')
class TestBun:

    @allure.title('Проверка типа данных и корректности имени булочки')
    @pytest.mark.parametrize('name, price', Data.list_buns)
    def test_get_name_return_correct_name(self, name, price, create_bun):
        assert type(create_bun.get_name()) == str and create_bun.get_name() == name

    @allure.title('Проверка типа данных и корректности цены булочки')
    @pytest.mark.parametrize('name, price', Data.list_buns)
    def test_get_price_return_correct_price(self, name, price, create_bun):
        assert type(create_bun.get_price()) == float and create_bun.get_price() == price

    @allure.title('Проверка создания булочки')
    @pytest.mark.parametrize('name, price', Data.list_buns)
    def test_init_return_correct_data(self, name, price, create_bun):
        assert create_bun.name == name and create_bun.price == price

