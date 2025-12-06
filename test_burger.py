import pytest
from burger import Burger
from data import Ingredients


class TestBurger:

    def test_set_buns_add_bun_at_order(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_add_ingriedient_at_order(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_sauce

    def test_remove_ingredient_remove_ingredient_from_order(self, burger):
        burger.ingredients = [Ingredients.sauce, Ingredients.filling]
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients == [Ingredients.filling]
