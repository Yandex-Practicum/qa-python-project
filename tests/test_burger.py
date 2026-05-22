import pytest
from unittest.mock import Mock


class TestBurger:

    def test_init_burger_has_empty_ingredients_and_no_bun(self, burger):

        assert burger.bun is None
        assert burger.ingredients == []


    def test_set_buns(self, burger, mock_bun):

        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun


    def test_add_ingredient(self, burger, mock_ingredient_sauce):

        burger.add_ingredient(mock_ingredient_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_sauce


    def test_remove_ingredient(self, burger, mock_ingredient_sauce):

        burger.add_ingredient(mock_ingredient_sauce)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0


    def test_move_ingredient(self, burger, mock_ingredient_sauce, mock_ingredient_filling):

        burger.add_ingredient(mock_ingredient_sauce)   
        burger.add_ingredient(mock_ingredient_filling) 

        burger.move_ingredient(1, 0)

        assert burger.ingredients[0] == mock_ingredient_filling
        assert burger.ingredients[1] == mock_ingredient_sauce


    @pytest.mark.parametrize(
        "bun_price, sauce_price, filling_price, expected_total",[
            (100.0, 50.0, 150.0, 400.0),  # 100*2 + 50 + 150 = 400
            (0.0, 0.0, 0.0, 0.0)          # Бесплатный бургер
        ])
    def test_get_price(self, burger, bun_price, sauce_price, filling_price, expected_total):

        mock_bun_dyn = Mock()
        mock_bun_dyn.get_price.return_value = bun_price

        mock_sauce_dyn = Mock()
        mock_sauce_dyn.get_price.return_value = sauce_price

        mock_filling_dyn = Mock()
        mock_filling_dyn.get_price.return_value = filling_price

        burger.set_buns(mock_bun_dyn)
        burger.add_ingredient(mock_sauce_dyn)
        burger.add_ingredient(mock_filling_dyn)

        assert burger.get_price() == expected_total


    def test_get_receipt(self, burger, mock_bun, mock_ingredient_sauce):

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)

        expected_receipt = (
            f"(==== {mock_bun.get_name()} ====)\n"
            f"= {mock_ingredient_sauce.get_type().lower()} {mock_ingredient_sauce.get_name()} =\n"
            f"(==== {mock_bun.get_name()} ====)\n\n"
            f"Price: {burger.get_price()}")

        assert burger.get_receipt() == expected_receipt
