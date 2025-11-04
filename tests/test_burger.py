import pytest
from unittest.mock import Mock
from praktikum.ingredient import Ingredient


class TestBurger:
    
    def test_set_buns_bun_mock_sets_bun_correctly(self, burger, bun_mock):
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient_mock_adds_to_ingredient_list(self, burger, ingredient_mock):
        burger.add_ingredient(ingredient_mock)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_mock

    def test_remove_ingredient_existing_ingredient_removes_from_list(self, burger, ingredient_mock):
        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient_valid_index_change_order(self, burger, ingredient_mock):
        second_ingredient = Mock(spec=Ingredient)
        second_ingredient.get_name.return_value = 'second ingredient'

        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(second_ingredient)

        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == second_ingredient
        assert burger.ingredients[1] == ingredient_mock

    def test_get_price_bun_and_ingredient_returns_correct_total(self, burger, bun_mock, ingredient_mock):
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)

        expected_price = bun_mock.get_price() * 2 + ingredient_mock.get_price()
        assert burger.get_price() == expected_price

    def test_get_receipt_with_bun_and_ingredient_returns_correct_reciept(self, burger, bun_mock, ingredient_mock):
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)

        receipt = burger.get_receipt()
        assert '(==== test bun ====)' in receipt
        assert '= sauce test ingredient =' in receipt
        assert 'Price: 300' in receipt