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

    def test_set_buns(self):
        """Тест 2: Установка булочки"""
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Test Bun"
        mock_bun.get_price.return_value = 50.0

        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun, "Булочка должна сохраниться в объекте"
        assert burger.bun.get_name() == "Test Bun", "Название булочки должно совпадать"
        assert burger.bun.get_price() == 50.0, "Цена булочки должна совпадать"