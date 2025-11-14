from unittest.mock import Mock

import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


class TestBurger:

    # Проверить, что булочка добавлена в бургер
    def test_check_set_buns(self):
        burger = Burger()
        bun = Bun('Краторная булка N-200i', 1255)
        burger.set_buns(bun)
        assert burger.bun == bun

    # Проверить, что ингредиенты добавляются в бургер
    def test_check_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус фирменный Space Sauce', 80)
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    # Проверить, что можно добавить несколько ингредиентов в бургер
    def test_check_some_add_ingredients(self):
        burger = Burger()
        ingredient_1 = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус фирменный Space Sauce', 80)
        ingredient_2 = Ingredient(INGREDIENT_TYPE_FILLING, 'Биокотлета из марсианской Магнолии', 424)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        assert len(burger.ingredients) == 2

    # Проверить, что ингредиент можно удалить
    def test_check_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    # Проверить, что ингредиенты можно перемещать
    def test_check_move_ingredient(self):
        burger = Burger()
        ingredient_1 = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус фирменный Space Sauce', 80)
        ingredient_2 = Ingredient(INGREDIENT_TYPE_FILLING, 'Биокотлета из марсианской Магнолии', 424)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] is ingredient_1

    # Проверить, что цена корректно рассчитывается
    def test_check_get_price(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 120
        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_price.return_value = 80
        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_price.return_value = 30

        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]
        price = burger.get_price()
        assert price == 350

    # Проверить получение рецепта
    def test_check_get_receipt(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Флюоресцентная булка R2-D3'
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'Биокотлета из марсианской Магнолии'
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING

        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        burger.get_price = Mock(return_value=300.0)
        receipt = burger.get_receipt()
        expected_receipt = "(==== Флюоресцентная булка R2-D3 ====)\n"\
                           "= filling Биокотлета из марсианской Магнолии =\n"\
                           "(==== Флюоресцентная булка R2-D3 ====)\n\n"\
                           "Price: 300.0"
        assert receipt == expected_receipt