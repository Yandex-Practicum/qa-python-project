import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from praktikum.bun import Bun


class TestBun:
    def setup_method(self):
        self.bun = Bun("Булочка", 100.0)
    
    def test_get_name(self):
        """Тестируем получение названия булочки"""
        assert self.bun.get_name() == "Булочка"
    
    def test_get_price(self):
        """Тестируем получение цены булочки"""
        assert self.bun.get_price() == 100.0
    
    @pytest.mark.parametrize("name,price", [
        ("Ржаная булочка", 150.0),
        ("Булочка с кунжутом", 120.0),
        ("Белая булочка", 90.0)
    ])
    def test_bun_initialization(self, name, price):
        """Тестируем инициализацию булочки с разными параметрами"""
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price