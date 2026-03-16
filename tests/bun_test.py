import pytest
from praktikum.bun import Bun

class TestBun:

    def test_bun_initialization_sets_name_correctly(self):
        bun = Bun("black bun", 100)
        assert bun.name == "black bun"

    def test_bun_initialization_sets_price_correctly(self):
        bun = Bun("black bun", 100)
        assert bun.price == 100

    def test_get_name_returns_correct_name(self):
        bun = Bun("white bun", 200)
        assert bun.get_name() == "white bun"

    def test_get_price_returns_correct_price(self):
        bun = Bun("red bun", 300)
        assert bun.get_price() == 300

    @pytest.mark.parametrize("name, price", [
        ("very long name of a bun", 99.99),
        ("", 0),
        ("bun with special symbols %$#", -50)  
    ])
    def test_bun_creation_with_various_parameters(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price