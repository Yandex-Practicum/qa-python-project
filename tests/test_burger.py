from unittest.mock import Mock
from praktikum.burger import Burger
from static_data import Data
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


class TestBurger:

    # Test set_buns() method
    def test_set_buns(self):
        burger = Burger()
        bun = Bun(Data.WHITE_BUN, Data.WHITE_BUN_PRICE)
        burger.set_buns(bun)
        assert burger.bun == bun

    # Test adding component with mocking
    def test_add_component(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 100
        mock_ingredient.get_name.return_value = 'cutlet'
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].get_price() == 100
        assert burger.ingredients[0].get_name() == 'cutlet'
        assert burger.ingredients[0].get_type() == INGREDIENT_TYPE_FILLING

    # Test remove_ingredient() method
    def test_remove_component(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    # Test get_price() method
    def test_get_price(self):
        burger = Burger()
        data = Database()
        burger.set_buns(data.available_buns()[0])
        burger.add_ingredient(data.available_ingredients()[0])
        burger.add_ingredient(data.available_ingredients()[1])
        burger.add_ingredient(data.available_ingredients()[2])
        assert burger.get_price() == 800

    # Test get_receipt() method
    def test_get_billing_cheque(self):
        burger = Burger()
        data = Database()
        burger.set_buns(data.available_buns()[2])
        burger.add_ingredient(data.available_ingredients()[0])
        burger.add_ingredient(data.available_ingredients()[1])
        burger.add_ingredient(data.available_ingredients()[2])
        expected_result = '''(==== red bun ====)\n= sauce hot sauce =\n= sauce sour cream =\n= sauce chili sauce =\n(==== red bun ====)\n\nPrice: 1200'''
        assert burger.get_receipt() == expected_result

    # Test move_ingredient() method
    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient_first = Mock()
        mock_ingredient_first.get_price.return_value = 100
        mock_ingredient_first.get_name.return_value = 'cutlet'
        mock_ingredient_first.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient_first)

        mock_ingredient_second = Mock()
        mock_ingredient_second.get_price.return_value = 300
        mock_ingredient_second.get_name.return_value = 'sausage'
        mock_ingredient_second.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient_second)

        burger.move_ingredient(0, 1)

        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_ingredient_second
        assert burger.ingredients[1] == mock_ingredient_first
