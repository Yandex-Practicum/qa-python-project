import pytest
from pages.burger import Burger
from pages.ingredient import Ingredient
from pages.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_set_buns_sets_bun_property(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun())
        assert burger.bun is not None

    def test_add_ingredient_adds_to_list(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient())
        assert len(burger.ingredients) == 1

    def test_remove_ingredient_removes_by_index(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient())
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient_moves_position(self, mock_ingredient):
        burger = Burger()
        ingredients = [
            mock_ingredient(name="one"),
            mock_ingredient(name="two"),
            mock_ingredient(name="three")
        ]
        for ing in ingredients:
            burger.add_ingredient(ing)
        burger.move_ingredient(0, 2)
        assert burger.ingredients[0].get_name() == "two"
        assert burger.ingredients[2].get_name() == "one"

    def test_get_price_calculates_total(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun(price=100))
        burger.add_ingredient(mock_ingredient(price=50))
        burger.add_ingredient(mock_ingredient(price=100))
        assert burger.get_price() == 350

    def test_get_receipt_returns_correct_string(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun(name="Red Bun"))
        burger.add_ingredient(mock_ingredient(name="Cheese", ingredient_type=INGREDIENT_TYPE_SAUCE))
        burger.add_ingredient(mock_ingredient(name="Beef", ingredient_type=INGREDIENT_TYPE_FILLING))

        expected = "(==== Red Bun ====)\n= sauce Cheese =\n= filling Beef =\n(==== Red Bun ====)\nPrice: 250"
        assert burger.get_receipt() == expected