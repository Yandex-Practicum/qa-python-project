import pytest

from praktikum.bun import Bun

class TestBun:
    """Тесты для класса Bun"""

    @pytest.mark.parametrize("name,price", [
        ("Краторная булка", 100.0),
        ("Ядерная булка", 200.0),
    ])
    def test_bun_initialization(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    def test_get_name(self):
        test_bun = Bun("Белая булочка", 500)
        assert test_bun.get_name() == "Белая булочка"

    def test_get_price(self):
        test_bun = Bun("Чёрная булочка", 750.5)
        assert test_bun.get_price() == 750.5