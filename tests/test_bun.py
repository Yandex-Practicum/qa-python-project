import pytest
from praktikum.bun import Bun


class TestBunCreation:
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200.5),
        ("red bun", 0),
    ])
    def test_bun_creation(self, name, price):
        """Проверяет корректное создание булочек с разными значениями."""
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price


class TestBunGetters:
    @pytest.mark.parametrize("name", ["cheese bun", "gluten-free bun"])
    def test_get_name(self, name):
        """Проверяет корректное наименование булочек."""
        bun = Bun(name, 123)
        assert bun.get_name() == name

    @pytest.mark.parametrize("price", [10, 0.99, 300])
    def test_get_price(self, price):
        """Проверяет корректную стоимость."""
        bun = Bun("test bun", price)
        assert bun.get_price() == price
