from unittest.mock import Mock
import pytest
from data import BurgerSample
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_set_buns_success(self, burger):
        burger.set_buns(BurgerSample.BUN_NAME)
        assert burger.bun == BurgerSample.BUN_NAME

    def test_add_ingredient_success(self, burger):
        burger.add_ingredient(BurgerSample.SAUCE_NAME)
        assert BurgerSample.SAUCE_NAME in burger.ingredients

    def test_remove_ingredient_success(self, burger):
        burger.add_ingredient(BurgerSample.SAUCE_NAME)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient_success(self, burger):
        burger.add_ingredient(BurgerSample.SAUCE_NAME)
        burger.add_ingredient(BurgerSample.FILLING_NAME)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == BurgerSample.FILLING_NAME

    @pytest.mark.parametrize('bun_name, bun_price, sauce_name, sauce_price, filling_name, filling_price, total',
                             [BurgerSample.BURGER1,
                              BurgerSample.BURGER2])
    def test_get_price_success(self, burger,
                               bun_name,
                               bun_price,
                               sauce_name,
                               sauce_price,
                               filling_name,
                               filling_price,
                               total):
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = bun_price

        mock_sauce = Mock()
        mock_sauce.get_name.return_value = sauce_name
        mock_sauce.get_price.return_value = sauce_price

        mock_filling = Mock()
        mock_filling.get_name.return_value = filling_name
        mock_filling.get_price.return_value = filling_price

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert burger.get_price() == total

    @pytest.mark.parametrize('bun_name, bun_price, sauce_name, sauce_price, filling_name, filling_price, total',
                             [BurgerSample.BURGER1,
                              BurgerSample.BURGER2])
    def test_get_receipt(self, burger,
                         bun_name,
                         bun_price,
                         sauce_name,
                         sauce_price,
                         filling_name,
                         filling_price,
                         total):
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = bun_price

        mock_sauce = Mock()
        mock_sauce.get_name.return_value = sauce_name
        mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_sauce.get_price.return_value = sauce_price

        mock_filling = Mock()
        mock_filling.get_name.return_value = filling_name
        mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_filling.get_price.return_value = filling_price

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert bun_name and sauce_name and filling_name and str(total) in burger.get_receipt()
        