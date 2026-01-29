import allure
import pytest

from bun import Bun
from data import BurgerInfo as b


class TestBun:
    """
    Тесты методов класса Bun.
    """

    @allure.title('Проверяем конструктор __init__() с пустым и незаданным названием булки')
    @pytest.mark.parametrize('name', ['', None])
    def test_init_bun_name(self, name):
        bun = Bun(name, b.BUN_PRICE)
        assert bun.name == name

    @allure.title('Проверяем конструктор __init__() с нулевой и незаданной стоимостью булки')
    @pytest.mark.parametrize('price', [0.0, None])
    def test_init_bun_price(self, price):
        bun = Bun(b.BUN_NAME, price)
        assert bun.price == price

    @allure.title('Проверяем метод get_name() - получить название булки')
    def test_get_name(self):
        bun = Bun(b.BUN_NAME, b.BUN_PRICE)
        assert bun.get_name() == b.BUN_NAME

    @allure.title('Проверяем метод get_price() - получить стоимость булки')
    def test_get_price(self):
        bun = Bun(b.BUN_NAME, b.BUN_PRICE)
        assert bun.get_price() == b.BUN_PRICE

