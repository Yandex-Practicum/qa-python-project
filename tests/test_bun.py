import pytest
from praktikum.bun import Bun
from data import BunTestData


class TestBun:

    @pytest.mark.parametrize("bun_data", [
        BunTestData.VALID_BUN,
        BunTestData.VALID_BUN_2,
        BunTestData.EMPTY_NAME_BUN,
    ])
    def test_bun_creation(self, bun_data):
        """Тест проверяет инициализацию объекта Bun через прямые атрибуты"""
        bun = Bun(bun_data["name"], bun_data["price"])
        
        assert bun.name == bun_data["name"]
        assert bun.price == bun_data["price"]

    def test_bun_get_name(self):
        """Тест проверяет метод get_name()"""
        bun_data = BunTestData.VALID_BUN
        bun = Bun(bun_data['name'], bun_data['price'])
        assert bun.get_name() == bun_data['name']

    def test_bun_get_price(self):
        """Тест проверяет метод get_price()"""
        bun_data = BunTestData.VALID_BUN_2
        bun = Bun(bun_data['name'], bun_data['price'])
        assert bun.get_price() == bun_data['price']