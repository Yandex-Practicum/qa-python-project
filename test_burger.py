import pytest
from data import order_data
from unittest.mock import Mock
from burger import Burger
from bun import Bun
from ingredient import Ingredient

class TestBurger:

    def test_set_buns_add_bun_at_order(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_add_ingriedient_at_order(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_sauce

    def test_remove_ingredient_remove_ingredient_from_order(self, burger, mock_sauce, mock_filling):        
        burger.ingredients = [mock_sauce, mock_filling]
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients == [mock_filling]

    def test_move_ingredient_swaps_positions_of_ingredients(self, burger, mock_sauce, mock_filling):
        burger.ingredients = [mock_sauce, mock_filling]
        burger.move_ingredient(1, 0)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_filling
        assert burger.ingredients[1] == mock_sauce

    @pytest.mark.parametrize("bun_value, sauce_value, filling_value, expected_price", 
                             [order_data.price_without_order,
                              order_data.price_of_order_with_bun,
                              order_data.price_of_order_with_ingredient,
                              order_data.price_of_order_with_two_ingredients,
                              order_data.price_of_order_with_bun_and_ingredient,
                              order_data.price_of_order_with_bun_and_two_ingredients
                              ]
                            )
    def test_get_price_calculate_price_of_order(self,burger, bun_value, sauce_value, filling_value, expected_price):
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_value
        mock_sauce = Mock()
        mock_sauce.get_price.return_value = sauce_value
        mock_filling = Mock()
        mock_filling.get_price.return_value = filling_value
        burger.bun = mock_bun
        burger.ingredients = [mock_sauce, mock_filling]
        assert burger.get_price() == expected_price

