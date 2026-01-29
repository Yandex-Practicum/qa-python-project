import collections
from unittest.mock import Mock

import pytest

from data import generator_ingredients
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient_types import *


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun = Bun('test_name', 10)
        burger.set_buns(bun)
        assert burger.bun == bun

    @pytest.mark.parametrize('count_ingredient', [1, 3])
    def test_add_ingredient_for_burger(self, count_ingredient):
        burger = Burger()
        test_ingredients = generator_ingredients(count_ingredient)  # Генерируем тестовые ингредиенты
        # Добавляем ингредедиенты в бургер
        for test_ingredient in test_ingredients:
            burger.add_ingredient(test_ingredient)
        assert burger.ingredients == test_ingredients

    @pytest.mark.parametrize('index_remove', [0, 1, -1])
    def test_remove_ingredient_from_burger(self, index_remove, fixt_set_burger):
        """ удаляем в тестах граничные значения (1ый, средний, последний)"""
        burger = fixt_set_burger
        test_ingredients = burger.ingredients.copy()

        test_ingredients.pop(index_remove)  # Удаляем из тестового набора
        burger.remove_ingredient(index_remove)  # Удаляем методом класса
        assert burger.ingredients == test_ingredients

    @pytest.mark.parametrize('old_index, new_index', [[0, 1], [0, 2], [1, 2]])
    def test_move_ingredient_in_burger_check_index(self, old_index, new_index, fixt_set_burger):
        burger = fixt_set_burger
        move_value = burger.ingredients[old_index]
        burger.move_ingredient(old_index, new_index)
        assert burger.ingredients.index(move_value) == new_index

    @pytest.mark.parametrize('old_index, new_index', [[0, 1], [0, 2], [1, 2]])
    def test_move_ingredient_in_burger_data_integrity(self, old_index, new_index, fixt_set_burger):
        burger = fixt_set_burger
        ingredients_before_move = burger.ingredients.copy()
        burger.move_ingredient(old_index, new_index)
        # проверяет целостность данных до и после перемещения (порядок не важен)
        assert collections.Counter(burger.ingredients) == collections.Counter(ingredients_before_move)

    @pytest.mark.parametrize("bun_price, ingredient_price", [(10, 0), (10, 5)])
    def test_get_price_for_burger(self, bun_price, ingredient_price):
        """
        2 теста - без/с ингредиентами
        """
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = ingredient_price

        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient, mock_ingredient]

        expected_price = bun_price * 2 + ingredient_price * 2
        actual_price = burger.get_price()
        assert expected_price == actual_price

    def test_get_receipt_check_bun_name(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "test_name_bun"
        mock_bun.get_price.return_value = 10

        burger = Burger()
        burger.set_buns(mock_bun)

        receipt = burger.get_receipt()
        excepted = f"(==== {mock_bun.get_name()} ====)"
        assert excepted in receipt

    def test_get_receipt_check_ingredient_name(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "test_name_bun"
        mock_bun.get_price.return_value = 10

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = "test_name_ingredient"
        mock_ingredient.get_price.return_value = 5

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()
        expected = f'= {mock_ingredient.get_type().lower()} {mock_ingredient.get_name()} ='
        assert expected in receipt
