# test_bun.py
import pytest
import allure
from bun import Bun

@allure.feature('Bun')
class TestBun:

    @allure.title('Сохраняем name при создании булки')
    def test_init_saves_name(self):
        with allure.step('Создать булку (name="black bun", price=100)'):
            bun = Bun("black bun", 100)

        assert bun.name == "black bun", f"Ожидалось 'black bun', получено '{bun.name}'"

    @allure.title('Сохраняем price при создании булки')
    def test_init_saves_price(self):
        with allure.step('Создать булку (name="black bun", price=100)'):
            bun = Bun("black bun", 100)

        assert bun.price == 100, f"Ожидалось 100, получено {bun.price}"

    @pytest.mark.parametrize('name, price', [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
    ])
    @allure.title('get_name возвращает имя — {name}')
    def test_get_name_returns_correct_name(self, name, price):
        with allure.step('Создать булку'):
            bun = Bun(name, price)

        assert bun.get_name() == name, f"get_name() вернул '{bun.get_name()}', ожидалось '{name}'"

    @pytest.mark.parametrize('name, price', [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
    ])
    @allure.title('get_price возвращает цену — {price}')
    def test_get_price_returns_correct_price(self, name, price):
        with allure.step('Создать булку'):
            bun = Bun(name, price)

        assert bun.get_price() == price, f"get_price() вернул {bun.get_price()}, ожидалось {price}"



