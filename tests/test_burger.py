from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
import pytest


class TestBurger:

    def test_create_new_burger_bun_name_is_None(self, burger):
        assert burger.bun is None

    def test_create_new_burger_ingredients_is_empty_list(self, burger):
        assert burger.ingredients == []

    def test_set_bun_choose_name_same_name_returned(self, burger):
        bun = Bun('Мягкая', 100)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient_choose_ingredient_added_to_the_ingredient_list(self, burger):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'hot sauce', 20)
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient_add_several_remove_one_returned_without_removed_one(self, burger):
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, 'Лук', 10))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, 'Томат', 20))
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1

    @pytest.mark.parametrize('index, expected_type', [
        (0, INGREDIENT_TYPE_SAUCE),
        (1, INGREDIENT_TYPE_FILLING)
    ])
    def test_move_ingredient_changes_order_of_ingredients_last_added_is_first(self, burger, index, expected_type):
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, 'Лук', 10))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, 'Томат', 20))
        burger.move_ingredient(0, 1)

        assert len(burger.ingredients) == 2 and burger.ingredients[index].type == expected_type

    def test_get_price_calculates_price_bun_plus_two_ingredients(self, burger):
        burger.set_buns(Bun('Мягкая', 50))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, 'Майонез', 20))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, 'Котлета', 100))
        assert burger.get_price() == 220

    def test_get_receipt_creates_receipt_bun_and_two_ingredients(self, burger):
        burger.set_buns(Bun('Мягкая', 50))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, 'Майонез', 20))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, 'Котлета', 100))

        expected_receipt = (
            "(==== Мягкая ====)\n"
            "= sauce Майонез =\n"
            "= filling Котлета =\n"
            "(==== Мягкая ====)\n\n"
            "Price: 220"
        )
        assert burger.get_receipt() == expected_receipt
