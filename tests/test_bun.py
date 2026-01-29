from praktikum.bun import Bun
import allure
import pytest


class TestBun:

    """
    ТЕСТЫ МЕТОДОВ КЛАССА Bun
    """

    @allure.title('Проверяем метод get_name() - получить название булочки')
    def test_get_name(self):
        bun = Bun('Злаковая', 5)
        assert bun.get_name() == 'Злаковая'

    @allure.title('Проверяем конструктор __init__() с незаданным названием булочки')
    @pytest.mark.parametrize('name', [''])
    def test_init_bun_name(self, name):
        bun = Bun(' ', 4.0)
        assert bun.get_name() == ' '

    @allure.title('Проверяем конструктор __init__() c нулевой стоимостью булочки')
    @pytest.mark.parametrize('price', [0.0])
    def test_init_bun_price_null(self, price):
        bun = Bun('Сырная', 0.0)
        assert bun.get_price() == 0.0

    @allure.title('Проверяем метод get_price - получить стоимость булочки')
    def test_get_price(self):
        bun = Bun('Луковая', 5.0)
        assert bun.get_price() == 5.0
