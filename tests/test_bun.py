import pytest
from praktikum.bun import Bun

class TestBun:
    @pytest.mark.parametrize("name, price", [
        ("КосмоБулка", 55.00),
        ("Сырная булочка", 30.00),
        ("Острая булочка", 25.50)
    ])
    def test_bun_initialization_name(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name

    @pytest.mark.parametrize("name, price", [
        ("КосмоБулка", 55.00),
        ("Сырная булочка", 30.00),
        ("Острая булочка", 25.50)
    ])
    def test_bun_initialization_price(self, name, price):
        bun = Bun(name, price)
        assert bun.price == price

    @pytest.mark.parametrize("name, price", [
        ("КосмоБулка", 55.00),
        ("Сырная булочка", 30.00),
        ("Острая булочка", 25.50)
    ])
    def test_bun_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", [
        ("КосмоБулка", 55.00),
        ("Сырная булочка", 30.00),
        ("Острая булочка", 25.50)
    ])
    def test_bun_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price




