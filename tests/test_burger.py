import pytest
from unittest.mock import Mock
from data import DataForTestPrice

class TestBurger:

    def test_set_bun(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun
        assert burger.bun.get_name() == "Урановая булка"
        assert burger.bun.get_price() == 50.0

    def test_add_ingredient(self, burger, ingredient_sauce):
        burger.add_ingredient(ingredient_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].get_name() == "Святящаяся горчица"
        assert burger.ingredients[0].get_type() == "SAUCE"
        assert burger.ingredients[0].get_price() == 10.0

    def test_remove_ingredient(self, burger, ingredient_filling, ingredient_sauce):
        burger.add_ingredient(ingredient_filling)
        burger.add_ingredient(ingredient_sauce)
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_filling
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger, ingredient_sauce, ingredient_filling):
        ingredient1 = ingredient_filling
        ingredient2 = ingredient_sauce

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient2
        assert burger.ingredients[1] == ingredient1

    @pytest.mark.parametrize("ingredient_data, expected_price", [DataForTestPrice.FIRST_SET, DataForTestPrice.SECOND_SET])
    def test_get_price(self, burger, bun, ingredient_data, expected_price):
        burger.set_buns(bun)
        for ingredient_type, name, price in ingredient_data:
            ingredient_mock = Mock()
            ingredient_mock.get_name.return_value = name
            ingredient_mock.get_type.return_value = ingredient_type
            ingredient_mock.get_price.return_value = price
            burger.add_ingredient(ingredient_mock)
        assert burger.get_price() == expected_price

    def test_get_receipt(self, burger, bun, ingredient_filling, ingredient_sauce):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_filling)
        burger.add_ingredient(ingredient_sauce)

        final_price = bun.get_price() * 2 + ingredient_filling.get_price() + ingredient_sauce.get_price()

        expected_receipt = (
            f"(==== {bun.get_name()} ====)\n"
            f"= filling {ingredient_filling.get_name()} =\n"
            f"= sauce {ingredient_sauce.get_name()} =\n"
            f"(==== {bun.get_name()} ====)\n\n"
            f"Price: {final_price}"
        )

        receipt = burger.get_receipt()
        assert receipt == expected_receipt
