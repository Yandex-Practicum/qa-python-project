import pytest
from praktikum.bun import Bun

class TestBun:

    # Параметризация включает в себя валидные и граничные значения
    @pytest.mark.parametrize("name, price", [
        ("craterous bun", 1255),
        ("fluorescent bun", 988),
        ("", 0)
    ])

    # Проверка что булочке можно назначить название и цену и будет возвращено корректное название и цена
    def test_bun_get_name_and_get_price_success(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name and bun.get_price() == price