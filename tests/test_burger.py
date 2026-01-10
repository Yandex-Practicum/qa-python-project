import pytest
from data import *
from praktikum.ingredient_types import *


class TestBurger:
    def test_burger_set_buns(self, burger):
        bun = make_mock(get_random_value(BUNS_NAMES), get_random_value(PRICES))
        burger.set_buns(bun)

        assert burger.bun == bun

    @pytest.mark.parametrize('ingredient_type', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_burger_add_ingredient(self, burger, ingredient_type):
        ingredients = ingredients_generator(ingredient_type)
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)

        assert burger.ingredients == ingredients

    def test_burger_remove_ingredient(self, burger):
        ingredient = make_mock(get_random_value(SAUCES_NAMES), get_random_value(PRICES), INGREDIENT_TYPE_SAUCE)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert not burger.ingredients

    def test_burger_move_ingredient(self, burger):
        first_ingredient = make_mock(get_random_value(SAUCES_NAMES), get_random_value(PRICES), INGREDIENT_TYPE_SAUCE)
        second_ingredient = make_mock(get_random_value(FILLINGS_NAMES), get_random_value(PRICES),
                                      INGREDIENT_TYPE_FILLING)
        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)
        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == second_ingredient and burger.ingredients[1] == first_ingredient

    def test_burger_get_price(self, burger):
        bun = make_mock(get_random_value(BUNS_NAMES), 100)
        first_ingredient = make_mock(get_random_value(SAUCES_NAMES), 200, INGREDIENT_TYPE_SAUCE)
        second_ingredient = make_mock(get_random_value(FILLINGS_NAMES), 300, INGREDIENT_TYPE_FILLING)
        burger.set_buns(bun)
        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)

        assert burger.get_price() == 700

    def test_burger_get_receipt(self, burger):
        result = "(==== black bun ====)\n= sauce hot sauce =\n= filling cutlet =\n(==== black bun ====)\n\nPrice: 700"
        bun = make_mock("black bun", 100)
        first_ingredient = make_mock("hot sauce", 200, INGREDIENT_TYPE_SAUCE)
        second_ingredient = make_mock("cutlet", 300, INGREDIENT_TYPE_FILLING)
        burger.set_buns(bun)
        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)

        assert burger.get_receipt() == result
