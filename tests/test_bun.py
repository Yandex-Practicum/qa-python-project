import pytest
from praktikum.bun import Bun

class TestBun:
    @pytest.mark.parametrize("name, price", [
        ("Флюоресцентная булка R2-D3", 988),
        ("Краторная булка N-200i", 1255)
    ])
    def test_bun_getters(self, name, price):
        bun = Bun(name=name, price=price)
        assert bun.get_name() == name
        assert bun.get_price() == price

    def test_bun_invalid_name(self):
        with pytest.raises(ValueError):
            Bun("", 100)  # Проверка на пустое название

    def test_bun_invalid_price(self):
        with pytest.raises(ValueError):
            Bun("Булка", -1)  # Проверка на отрицательную цену
