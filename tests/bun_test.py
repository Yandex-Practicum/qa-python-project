import pytest
import allure

from praktikum.bun import Bun


class TestBun:
    # В методе get_bun() не выполняются проверки числа перед созданием, он просто принимает float, поэтому
    # просто проверим общие границы
    @allure.title("Создание булочки")
    @pytest.mark.parametrize(
        "name,price",
        [
            ("white bun", 100),
            ("black bun", 200.0),
            ("red bun", 300),
            ("ноль bun", 0),
            ("negative bun", -50.5),
            ("nine булочка", 999999.99),
        ],
    )
    def test_get_bun(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price
