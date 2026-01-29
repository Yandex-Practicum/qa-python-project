import pytest
from praktikum.bun import Bun

class TestBun:
    def test_bun_initialization(self,bun_data): #инициализация_bun
        for bun in bun_data:
            assert isinstance(bun, Bun)
            assert bun.get_name() in ["black bun", "white bun", "red bun"]
            assert bun.get_price() in [100, 200, 300]

    @pytest.mark.parametrize("name, price", [("black bun", 100),("white bun", 200),("red bun", 300)])
    def test_bun_properties(self,bun_data, name, price): #тест_свойств_у_булок
        bun = next((i for i in bun_data if i.get_name() == name), None)
        assert bun is not None
        assert bun.get_name() == name
        assert bun.get_price() == price

    def test_bun_get_name(self,bun_data): #тест_метод_get_name
        for bun in bun_data:
            assert bun.get_name() == bun.name

    def test_bun_get_price(self,bun_data): #тест_метод_get_price
        for bun in bun_data:
            assert bun.get_price() == bun.price