import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize(
        "name, price",
        [
            ("Краторная булка", 300),
            ("Флюоресцентная булка", 999.99),
            ("", 150),  # Граничное значение: пустое имя
            ("Булка с кунжутом", 150)
        ]
    )
    # 1. Атомарный тест метода получения названия булочки
    def test_bun_get_name_returns_correct_value(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize(
        "name, price",
        [
            ("Краторная булка", 300),
            ("Флюоресцентная булка", 999.99),
            ("Обычная булка", 0),  # Граничное значение: нулевая цена
            ("Булка с кунжутом", 150)
        ]
    )
    # 2. Атомарный тест метода получения цены булочки
    def test_bun_get_price_returns_correct_value(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price

