import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    def test_set_buns_buns_set(self):
        bun = Bun("black bun", 100)
        burger = Burger()
        burger.set_buns(bun)
        assert "black bun" in burger.get_receipt()

    def test_add_ingredient_ingredient_added(self):
        bun = Bun("black bun", 100)
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert "hot sauce" in burger.get_receipt()

    def test_remove_ingredient_ingredient_removed(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.set_buns.return_value = ("black bun", 100)
        mock_ing_sauce = Mock()
        mock_ing_sauce.add_ingredient.return_value = (INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        mock_ing_filling = Mock()
        mock_ing_filling.add_ingredient.return_value = (INGREDIENT_TYPE_FILLING, "cutlet", 100)
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing_sauce)
        burger.add_ingredient(mock_ing_filling)
        burger.remove_ingredient(1)
        assert mock_ing_filling not in burger.ingredients

    def test_move_ingredient_ingredient_moved(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.set_buns.return_value = ("black bun", 100)
        mock_ing_filling = Mock()
        mock_ing_filling.add_ingredient.return_value = (INGREDIENT_TYPE_FILLING, "cutlet", 100)
        mock_ing_sauce_first = Mock()
        mock_ing_sauce_first.add_ingredient.return_value = (INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        mock_ing_sauce_second = Mock()
        mock_ing_sauce_second.add_ingredient.return_value = (INGREDIENT_TYPE_SAUCE, "sour cream", 200)
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing_filling)
        burger.add_ingredient(mock_ing_sauce_first)
        burger.add_ingredient(mock_ing_sauce_second)
        burger.move_ingredient(2, 0)
        assert burger.ingredients[0] == mock_ing_sauce_second

    def test_get_price_price_got(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.set_buns.return_value = ("black bun", 100)
        mock_ing_sauce = Mock()
        mock_ing_sauce.add_ingredient.return_value = (INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        mock_ing_filling = Mock()
        mock_ing_filling.add_ingredient.return_value = (INGREDIENT_TYPE_FILLING, "cutlet", 100)
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing_sauce)
        burger.add_ingredient(mock_ing_filling)
        mock_bun.get_price.return_value = 100
        mock_ing_sauce.get_price.return_value = 100
        mock_ing_filling.get_price.return_value = 100
        burger.get_price()
        assert burger.get_price() == 400

    def test_get_receipt_receipt_got(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.set_buns.return_value = ("black bun", 100)
        mock_ing_sauce = Mock()
        mock_ing_sauce.add_ingredient.return_value = (INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        mock_ing_filling = Mock()
        mock_ing_filling.add_ingredient.return_value = (INGREDIENT_TYPE_FILLING, "cutlet", 100)
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing_sauce)
        burger.add_ingredient(mock_ing_filling)
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100
        mock_ing_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ing_sauce.get_name.return_value = "hot sauce"
        mock_ing_sauce.get_price.return_value = 100
        mock_ing_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ing_filling.get_name.return_value = "cutlet"
        mock_ing_filling.get_price.return_value = 100
        assert burger.get_receipt() == ('(==== black bun ====)\n'
                                        '= sauce hot sauce =\n'
                                        '= filling cutlet =\n'
                                        '(==== black bun ====)\n'
                                        '\n'
                                        'Price: 400')
