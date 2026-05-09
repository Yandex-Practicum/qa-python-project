import pytest
from bun import Bun  # предполагаемый импорт, уточните по факту

class TestBun:

    @pytest.mark.parametrize("name, price", [
        ("Черная булочка", 100),
        ("Белая булочка", 80),
        ("Сладкая булочка", 120)
    ])
    def test_bun_creation(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price

    def test_get_name(self):
        bun = Bun("Обычная", 50)
        assert bun.get_name() == "Обычная"

    def test_get_price(self):
        bun = Bun("Особая", 200)
        assert bun.get_price() == 200