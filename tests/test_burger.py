import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


@pytest.fixture
def burger():
    return Burger()


class TestBurger:

    def test_constructor(self, burger):
        assert burger.bun is None
        assert len(burger.ingredients) == 0

    def test_set_buns_successfully_set(self, burger):
        bun = Mock(spec=Ingredient)
        burger.set_buns(bun)
        assert burger.bun is bun

    @pytest.mark.parametrize("ingredient", [Mock(spec=Ingredient), Mock(spec=Ingredient)])
    def test_add_ingredient_successfully_add(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_remove_ingredient_successfully_remove(self, burger):
        ingredient = Mock(spec=Ingredient)
        burger.ingredients = [ingredient]
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient_successfully_move(self, burger):
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        ingredient_3 = Mock()
        ingredient_4 = Mock()
        burger.ingredients = [ingredient_1, ingredient_2, ingredient_3, ingredient_4]
        burger.move_ingredient(0, 1)
        burger.move_ingredient(2, 3)
        assert burger.ingredients == [ingredient_2, ingredient_1, ingredient_4, ingredient_3]

    def test_get_price_successfully_get_price(self, burger):
        bun = Mock()
        bun.get_price.return_value = 10
        cheese = Mock(spec=Ingredient)
        cheese.get_price.return_value = 5
        burger.set_buns(bun)
        burger.add_ingredient(cheese)
        price = burger.get_price()
        assert price == 25

    def test_get_receipt_successfully_get_receipt(self, burger):
        bun = Mock()
        bun.get_name.return_value = 'Steakhouse'
        bun.get_price.return_value = 10.0
        burger.bun = bun
        ingredient = Mock()
        ingredient.get_type.return_value = 'sauce'
        ingredient.get_name.return_value = 'Ketchup'
        ingredient.get_price.return_value = 5
        burger.ingredients = [ingredient]
        receipt = burger.get_receipt()
        assert (bun.get_name.return_value in receipt
                and ingredient.get_type.return_value in receipt
                and ingredient.get_name.return_value in receipt
                and str(bun.get_price() * 2 + ingredient.get_price()) in receipt)
