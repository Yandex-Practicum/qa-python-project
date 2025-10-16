import pytest
from praktikum.bun import Bun


class TestBun:
    # Общие тестовые данные
    NAMES = [
        "sesame seed bun",  # булочка с пробелами
        "ночная булка",  # кириллица
        "BUN_UPPERCASE",  # верхний регистр
        "булка с пробелом",  # пробелы и кириллица
    ]

    PRICES = [
        99.99,  # дробная цена
        0,  # нулевая цена
        100,  # целая цена
        999.99,  # высокая цена
    ]

    # Тест для метода get_name()
    @pytest.mark.parametrize("name", NAMES)
    def test_get_name(self, name):
        bun = Bun(name, 100)  # цена фиксированная, так как не влияет на тест имени
        assert bun.get_name() == name

    # Тест для метода get_price()
    @pytest.mark.parametrize("price", PRICES)
    def test_get_price(self, price):
        bun = Bun("test bun", price)  # имя фиксированное, так как не влияет на тест цены
        assert bun.get_price() == price