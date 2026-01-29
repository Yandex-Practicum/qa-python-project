import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:

    @pytest.mark.parametrize('cake, price', [("MyOwnBun", 100.25)])
    def test_set_buns_successful_result(self, cake, price):
        burger = Bun(cake, price)
        super_burger = Burger()
        super_burger.set_buns(burger)
        assert burger == super_burger.bun

    @pytest.mark.parametrize("ingredient", [
        ([INGREDIENT_TYPE_FILLING, 'apple', 5.45]),
        ([INGREDIENT_TYPE_SAUCE, 'orange', 4.55])
    ])
    def test_add_ingredient_to_the_bun(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    @pytest.mark.parametrize("filling, sauce", [
        ([INGREDIENT_TYPE_FILLING, 'apple', 5.45],
        [INGREDIENT_TYPE_SAUCE, 'orange', 4.55])
    ])
    def test_remove_ingredient_from_the_bun(self, filling, sauce):
        burger = Burger()
        burger.ingredients = [filling, sauce]
        burger.remove_ingredient(0)
        assert filling not in burger.ingredients

    @pytest.mark.parametrize("filling, sauce", [
        ([INGREDIENT_TYPE_FILLING, 'apple', 5.45],
         [INGREDIENT_TYPE_SAUCE, 'orange', 4.55])
    ])
    def test_move_ingredient(self, filling, sauce):
        burger = Burger()
        burger.ingredients = [filling, sauce]
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [sauce, filling]

    def test_get_price_correct_cost(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 40.4
        mock_filling = Mock()
        mock_filling.get_price.return_value = 9.65
        mock_sauce = Mock()
        mock_sauce.get_price.return_value = 9.55
        burger.bun = mock_bun
        burger.ingredients = [mock_filling, mock_sauce]
        assert burger.get_price() == 100

    def test_get_receipt_correct_result(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "MyOwnBun"
        mock_filling = Mock()
        mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_filling.get_name.return_value = "MockFillingName"
        mock_sauce = Mock()
        mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_sauce.get_name.return_value = "MockSauceName"
        mock_burger = Mock()
        mock_burger.get_price.return_value = 100
        burger.bun = mock_bun
        burger.ingredients = [mock_filling, mock_sauce]
        burger.get_price = mock_burger.get_price
        expected_result = f'(==== MyOwnBun ====)\n' \
                          f'= filling MockFillingName =\n' \
                          f'= sauce MockSauceName =\n' \
                          f'(==== MyOwnBun ====)\n' \
                          f'\nPrice: 100'
        assert burger.get_receipt() == expected_result
