import pytest
from praktikum.bun import Bun

class TestBun:


    @pytest.mark.parametrize("name, price", [
        ("Black Bun", 100),
        ("White Bun", 50.5),
        ("", 0),
        ("Super Big Bun", 999.99)
    ])
    def test_bun_creation_and_getters(self, name, price):
        bun = Bun(name, price)
        # Проверяем, что конструктор сохранил данные (через атрибуты)
        assert bun.name == name
        assert bun.price == price
        # Проверяем работу геттеров
        assert bun.get_name() == name
        assert bun.get_price() == price


    def test_bun_attributes_modification(self):
        bun = Bun("Old Name", 100)
        bun.name = "New Name"
        bun.price = 200
        assert bun.get_name() == "New Name"
        assert bun.get_price() == 200