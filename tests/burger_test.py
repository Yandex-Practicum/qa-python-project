import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent))

from helpers import (
    create_mock_ingredient,
    create_mock_bun,
    add_multiple_ingredients_to_burger,
    calculate_burger_price,
    create_ingredients_list
)
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    
    def test_set_bun_success(self, burger, white_bun):
        burger.set_buns(white_bun)
        assert burger.bun == white_bun

    def test_set_bun_replace_existing(self, burger, white_bun, black_bun):
        burger.set_buns(white_bun)
        burger.set_buns(black_bun)
        assert burger.bun == black_bun

    def test_add_ingredient_one(self, burger, sauce_ingredient):
        burger.add_ingredient(sauce_ingredient)
        assert len(burger.ingredients) == 1

    def test_add_ingredient_first_element(self, burger, sauce_ingredient):
        burger.add_ingredient(sauce_ingredient)
        assert burger.ingredients[0] == sauce_ingredient

    def test_add_ingredient_multiple(self, burger, ingredient_count):
        ingredients = create_ingredients_list(ingredient_count, INGREDIENT_TYPE_SAUCE, 50.0)
        burger = add_multiple_ingredients_to_burger(burger, ingredients)
        assert len(burger.ingredients) == ingredient_count

    def test_add_ingredient_keeps_order_first(self, burger, sauce_ingredient, filling_ingredient):
        burger.add_ingredient(sauce_ingredient)
        burger.add_ingredient(filling_ingredient)
        assert burger.ingredients[0] == sauce_ingredient

    def test_add_ingredient_keeps_order_second(self, burger, sauce_ingredient, filling_ingredient):
        burger.add_ingredient(sauce_ingredient)
        burger.add_ingredient(filling_ingredient)
        assert burger.ingredients[1] == filling_ingredient

    
    def test_remove_ingredient_decreases_count(self, burger):
        ing1 = create_mock_ingredient("First", INGREDIENT_TYPE_SAUCE, 50.0)
        ing2 = create_mock_ingredient("Second", INGREDIENT_TYPE_FILLING, 100.0)
        burger = add_multiple_ingredients_to_burger(burger, [ing1, ing2])
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1

    def test_remove_ingredient_first_leaves_second(self, burger):
        ing1 = create_mock_ingredient("First", INGREDIENT_TYPE_SAUCE, 50.0)
        ing2 = create_mock_ingredient("Second", INGREDIENT_TYPE_FILLING, 100.0)
        burger = add_multiple_ingredients_to_burger(burger, [ing1, ing2])
        burger.remove_ingredient(0)
        assert burger.ingredients[0] == ing2

    def test_remove_ingredient_middle(self, burger):
        ing1 = create_mock_ingredient("First", INGREDIENT_TYPE_SAUCE, 50.0)
        ing2 = create_mock_ingredient("Middle", INGREDIENT_TYPE_FILLING, 100.0)
        ing3 = create_mock_ingredient("Last", INGREDIENT_TYPE_SAUCE, 75.0)
        burger = add_multiple_ingredients_to_burger(burger, [ing1, ing2, ing3])
        burger.remove_ingredient(1)
        assert burger.ingredients[1] == ing3

    def test_remove_ingredient_at_index(self, burger):
        ingredients = create_ingredients_list(3, INGREDIENT_TYPE_SAUCE, 50.0)
        burger = add_multiple_ingredients_to_burger(burger, ingredients)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 2

    def test_move_ingredient_forward(self, burger):
        ing1 = create_mock_ingredient("First", INGREDIENT_TYPE_SAUCE, 50.0)
        ing2 = create_mock_ingredient("Second", INGREDIENT_TYPE_FILLING, 100.0)
        ing3 = create_mock_ingredient("Third", INGREDIENT_TYPE_SAUCE, 75.0)
        burger = add_multiple_ingredients_to_burger(burger, [ing1, ing2, ing3])
        burger.move_ingredient(0, 2)
        assert burger.ingredients[2] == ing1

    def test_move_ingredient_changes_first_position(self, burger):
        ing1 = create_mock_ingredient("First", INGREDIENT_TYPE_SAUCE, 50.0)
        ing2 = create_mock_ingredient("Second", INGREDIENT_TYPE_FILLING, 100.0)
        ing3 = create_mock_ingredient("Third", INGREDIENT_TYPE_SAUCE, 75.0)
        burger = add_multiple_ingredients_to_burger(burger, [ing1, ing2, ing3])
        burger.move_ingredient(0, 2)
        assert burger.ingredients[0] == ing2

    def test_move_ingredient_backward(self, burger):
        ing1 = create_mock_ingredient("First", INGREDIENT_TYPE_SAUCE, 50.0)
        ing2 = create_mock_ingredient("Second", INGREDIENT_TYPE_FILLING, 100.0)
        ing3 = create_mock_ingredient("Third", INGREDIENT_TYPE_SAUCE, 75.0)
        burger = add_multiple_ingredients_to_burger(burger, [ing1, ing2, ing3])
        burger.move_ingredient(2, 0)
        assert burger.ingredients[0] == ing3

    def test_move_ingredient_preserves_count(self, burger):
       
        ingredients = create_ingredients_list(3, INGREDIENT_TYPE_SAUCE, 50.0)
        burger = add_multiple_ingredients_to_burger(burger, ingredients)
        burger.move_ingredient(0, 2)
        assert len(burger.ingredients) == 3

    
    @pytest.mark.parametrize("bun_price,ingredient_prices,expected_price", [
        (100.0, [50.0], 250.0),
        (150.0, [50.0, 75.0], 425.0),
        (200.0, [100.0, 100.0, 100.0], 700.0),
    ])
    def test_price_calculation(self, burger, bun_price, ingredient_prices, expected_price):
        calculated_price = calculate_burger_price(bun_price, ingredient_prices)
        assert calculated_price == expected_price

    
    @pytest.mark.parametrize("from_pos,to_pos", [
        (0, 1), (1, 0), (0, 2), (2, 0)
    ])
    def test_move_ingredient_parametrized(self, burger, from_pos, to_pos):
        ingredients = create_ingredients_list(3, INGREDIENT_TYPE_SAUCE, 50.0)
        burger = add_multiple_ingredients_to_burger(burger, ingredients)
        original_ingredient = burger.ingredients[from_pos]
        burger.move_ingredient(from_pos, to_pos)
        assert burger.ingredients[to_pos] == original_ingredient