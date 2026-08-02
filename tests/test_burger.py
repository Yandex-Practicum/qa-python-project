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

    def test_add_ingredient(self):
        """Тест 3: Добавление одного ингредиента"""
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = "Test Ingredient"
        mock_ingredient.get_price.return_value = 30.0
        mock_ingredient.get_type.return_value = "sauce"

        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1, "Должен быть 1 ингредиент"
        assert burger.ingredients[0] == mock_ingredient, "Ингредиент должен сохраниться"
        assert burger.ingredients[0].get_name() == "Test Ingredient"

    def test_add_multiple_ingredients(self):
        """Тест 4: Добавление нескольких ингредиентов"""
        mock_ing1 = Mock()
        mock_ing2 = Mock()
        mock_ing3 = Mock()

        burger = Burger()
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)
        burger.add_ingredient(mock_ing3)

        assert len(burger.ingredients) == 3, "Должно быть 3 ингредиента"
        assert burger.ingredients == [mock_ing1, mock_ing2, mock_ing3], "Порядок должен сохраняться"

    def test_remove_ingredient(self):
        """Тест 5: Удаление ингредиента по индексу"""
        mock_ing1 = Mock()
        mock_ing2 = Mock()
        mock_ing3 = Mock()

        burger = Burger()
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)
        burger.add_ingredient(mock_ing3)

        burger.remove_ingredient(1)  # Удаляем второй ингредиент

        assert len(burger.ingredients) == 2, "Должно остаться 2 ингредиента"
        assert burger.ingredients == [mock_ing1, mock_ing3], "Порядок должен сохраниться"