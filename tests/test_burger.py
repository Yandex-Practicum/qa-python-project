import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:
    #Тесты для класса Burger
    def test_init(self):
        """Тест 1: Проверка инициализации бургера"""
        burger = Burger()
        assert burger.bun is None, "Булочка должна быть None при инициализации"
        assert burger.ingredients == [], "Список ингредиентов должен быть пустым"