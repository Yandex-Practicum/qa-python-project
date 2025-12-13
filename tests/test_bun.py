"""Тесты для класса Bun"""
import pytest
from praktikum.bun import Bun
from tests.test_data import TEST_BUNS

class TestBun:
    """Тестовый класс для проверки класса Bun"""
    
    @pytest.mark.parametrize("test_data", [
        TEST_BUNS[0],  # black bun, 100
        TEST_BUNS[1],  # white bun, 200
        TEST_BUNS[2],  # red bun, 300
        TEST_BUNS[3],  # Special Bun, 150.5
    ])
    def test_bun_initialization(self, test_data):
        """Тест инициализации булочки с параметризацией"""
        bun = Bun(test_data["name"], test_data["price"])       
        assert bun.name == test_data["name"] and bun.price == test_data["price"]
    
    @pytest.mark.parametrize("test_data", [
        TEST_BUNS[4],  # Test Bun, 100.0
        TEST_BUNS[5],  # Another Bun, 0.0
        TEST_BUNS[6],  # Expensive Bun, 999.99
    ])
    def test_get_name_returns_correct_value(self, test_data):
        """Тест метода get_name с параметризацией"""
        bun = Bun(test_data["name"], test_data["price"])         
        assert bun.get_name() == test_data["name"]
    
    @pytest.mark.parametrize("test_data", [
        TEST_BUNS[7],  # Bun 1, 100.0
        TEST_BUNS[8],  # Bun 2, 0.0
        TEST_BUNS[9],  # Bun 3, 50.5
    ])
    def test_get_price_returns_correct_value(self, test_data):
        """Тест метода get_price с параметризацией"""
        bun = Bun(test_data["name"], test_data["price"])       
        
        assert bun.get_price() == test_data["price"]