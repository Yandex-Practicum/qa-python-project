import pytest
from praktikum.burger import Burger
from tests.data import TestData


class TestBurgerInit:
    """Тесты для конструктора класса Burger"""
    
    def test_burger_initialization(self, sample_burger):
        """Тест инициализации бургера"""
        assert sample_burger.bun is None
        assert sample_burger.ingredients == []