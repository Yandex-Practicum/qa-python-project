import pytest
from praktikum.bun import Bun


class TestBun:
    # Тесты для класса Bun
    
    def test_bun_creation_returns_correct_name(self):
        # Проверка: создание булочки возвращает правильное название
        bun = Bun("black bun", 100)
        assert bun.get_name() == "black bun"
    
    def test_bun_creation_returns_correct_price(self):
        # Проверка: создание булочки возвращает правильную цену
        bun = Bun("white bun", 200)
        assert bun.get_price() == 200
    
    @pytest.mark.parametrize("name, price", 
    [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
        ("", 0),
        ("special bun", 99.99),
    ])
    def test_bun_creation_with_different_params(self, name, price):
        # Параметризованный тест: создание булочек с разными параметрами"""
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price

        