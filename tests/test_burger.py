from unittest.mock import Mock
from praktikum.ingredient_types import *
from praktikum.bun import Bun

class TestBurger:
    def test_set_buns(self, burger):
        bun = Bun('some_name', 100)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self, burger):
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'Some_bun'
        mock_ingredient.get_price.return_value = 10
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].get_name() == 'Some_bun'
        assert burger.ingredients[0].get_price() == 10
        assert burger.ingredients[0].get_type() == INGREDIENT_TYPE_FILLING

    def test_remove_ingredient(self, burger):
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_get_price(self, burger, database):
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[3])
        assert burger.get_price() == 400.0
    
    def test_get_receipt(self, burger, database):
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[3])
        expected_receipt = "(==== black bun ====)\n"\
                           "= sauce hot sauce =\n"\
                           "= filling cutlet =\n"\
                           "(==== black bun ====)\n\n"\
                           "Price: 400"
        assert expected_receipt == burger.get_receipt()