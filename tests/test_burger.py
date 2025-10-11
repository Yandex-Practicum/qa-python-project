import pytest
import praktikum.ingredient_types
from praktikum.database import Database
from test_data import Data
from unittest.mock import Mock
from praktikum.burger import Burger, Bun


class TestBurger():

    # Тест init
    def test_burger_initialization(self):
        burger = Burger()
        assert burger.bun is None
        assert isinstance(burger.ingredients, list)
        assert len(burger.ingredients) == 0
        assert burger.ingredients == []

    # Тест метода set_buns
    def test_set_buns(self):
        burger=Burger()
        bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)
        burger.set_buns(bun)
        assert burger.bun == bun

    # Тест метода add_ingredient
    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = Data.BUN_NAME
        mock_ingredient.get_price.return_value = Data.BUN_PRICE
        mock_ingredient.get_type.return_value = praktikum.ingredient_types.INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    # Тест метода remove_ingredient
    def test_remove_ingredient(self):
        burger = Burger()
        ingredient_1st,ingredient_2nd,ingredient_3rd = Mock(),Mock(),Mock()
        burger.ingredients = [ingredient_1st, ingredient_2nd,ingredient_3rd]
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == ingredient_2nd

    # Тест метода move_ingredient
    def test_move_ingredient(self):
        burger = Burger()
        ingredient_1st,ingredient_2nd,ingredient_3rd = Mock(),Mock(),Mock()
        burger.ingredients = [ingredient_1st, ingredient_2nd, ingredient_3rd]
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [ingredient_2nd, ingredient_3rd, ingredient_1st]

    # Тест метода get_price
    @pytest.mark.parametrize(
        "bun_index, ingredient_indexes, expected_price",
        [
            (2, [2, 4], 1100.00),
            (0, [0, 3], 400.00),
            (1, [1, 5], 900.00),
            (2, [], 600.00),
            (0, [5], 500.00)
        ]
    )
    def test_get_price(self, bun_index, ingredient_indexes, expected_price):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[bun_index])
        for id in ingredient_indexes:
            burger.add_ingredient(database.available_ingredients()[id])
        assert burger.get_price() == expected_price


    # Тест метода get_receipt
    def test_get_receipt(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[2])
        burger.add_ingredient(database.available_ingredients()[2])
        burger.add_ingredient(database.available_ingredients()[4])
        expected_result = "(==== red bun ====)\n" \
                           "= sauce chili sauce =\n" \
                           "= filling dinosaur =\n" \
                           "(==== red bun ====)\n\n" \
                           "Price: 1100"
        assert expected_result == burger.get_receipt()