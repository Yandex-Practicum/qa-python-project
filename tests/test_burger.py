import pytest
from unittest.mock import Mock, patch
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from constsnts import Constants
from conftest import ingredient_fix, ingredient_filling_fix


class TestBurger:

    def test_burger_set_buns_successful(self, bun_fix):

        burger1 = Burger()
        burger1.set_buns(bun_fix)
        assert str(vars(burger1.bun)) == str(vars(bun_fix))

    def test_burger_add_ingredient_successful(self, ingredient_fix):

        burger1 = Burger()
        burger1.add_ingredient(ingredient_fix)
        assert str(vars(burger1.ingredients[-1])) == str(vars(ingredient_fix))

    def test_burger_remove_ingredient_successful(self, ingredient_fix):

        mock_add_ingredient = Mock()
        mock_add_ingredient.return_value = ingredient_fix
        burger1 = Burger()
        burger1.add_ingredient(mock_add_ingredient.return_value)
        burger1.remove_ingredient(-1)
        assert len(burger1.ingredients) == 0

    def test_burger_move_ingredient_successful(self, ingredient_fix, ingredient_filling_fix):

        burger1 = Burger()
        burger1.add_ingredient(ingredient_fix)
        burger1.add_ingredient(ingredient_filling_fix)
        burger1.move_ingredient(0, 1)
        assert burger1.ingredients[-1] == ingredient_fix

    @pytest.mark.parametrize('bun_data, ingredients_data, price',
                             [
                                 (['black bun', 100], ['SAUCE', 'sour cream', 200], 400),
                                 (['white bun', 200], ['FILLING', 'sausage', 300], 700),
                                 (['red bun', 300], ['FILLING', 'dinosaur', 200], 800)
                             ]
                             )
    def test_burger_get_price_successful(self, bun_data, ingredients_data, price):

        bun1 = Bun(*bun_data)
        ingredient1 = Ingredient(*ingredients_data)
        burger1 = Burger()
        burger1.set_buns(bun1)
        burger1.add_ingredient(ingredient1)
        assert burger1.get_price() == price

    def test_burger_get_receipt_successful(self):

        bun1 = Bun('black bun', 100)
        ingredient1 = Ingredient('FILLING', 'sausage', 300)
        ingredient2 = Ingredient('SAUCE', 'sour cream', 200)
        burger1 = Burger()
        burger1.set_buns(bun1)
        burger1.add_ingredient(ingredient1)
        burger1.add_ingredient(ingredient2)
        check = f"(==== black bun ====)\n= filling sausage =\n= sauce sour cream =\n(==== black bun ====)\n\nPrice: 700"
        assert burger1.get_receipt() == check
