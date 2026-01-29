import pytest

from Diplom_1.data import Data
from Diplom_1.ingredient import Ingredient


class TestIngredient():
    @pytest.mark.parametrize(
        "type, name, price, expected_price",
        [
            (Data.one_type, Data.sauce_one, Data.price_one, Data.price_one),
            (Data.one_type, Data.sauce_two, Data.price_two, Data.price_two),
            (Data.one_type, Data.sauce_three, Data.price_three, Data.price_three),
            (Data.two_type, Data.filling_one, Data.price_one, Data.price_one),
            (Data.two_type, Data.filling_two, Data.price_two, Data.price_two),
            (Data.two_type, Data.filling_three, Data.price_three, Data.price_three)
        ]
    )
    def test_get_price(self, type, name, price, expected_price):
        ingredient = Ingredient(type, name, price)

        assert ingredient.get_price() == expected_price


    @pytest.mark.parametrize(
        "type, name, price, expected_name",
        [
            (Data.one_type, Data.sauce_one, Data.price_one, Data.sauce_one),
            (Data.one_type, Data.sauce_two, Data.price_two, Data.sauce_two),
            (Data.one_type, Data.sauce_three, Data.price_three, Data.sauce_three),
            (Data.two_type, Data.filling_one, Data.price_one, Data.filling_one),
            (Data.two_type, Data.filling_two, Data.price_two, Data.filling_two),
            (Data.two_type, Data.filling_three, Data.price_three, Data.filling_three)
        ]
    )
    def test_get_name(self, type, name, price, expected_name):
        ingredient = Ingredient(type, name, price)

        assert ingredient.get_name()==expected_name


    @pytest.mark.parametrize(
        "type, name, price, expected_type",
        [
            (Data.one_type, Data.sauce_one, Data.price_one, Data.one_type),
            (Data.one_type, Data.sauce_two, Data.price_two, Data.one_type),
            (Data.one_type, Data.sauce_three, Data.price_three, Data.one_type),
            (Data.two_type, Data.filling_one, Data.price_one, Data.two_type),
            (Data.two_type, Data.filling_two, Data.price_two, Data.two_type),
            (Data.two_type, Data.filling_three, Data.price_three, Data.two_type)
        ]
    )
    def test_get_type(self, type, name, price, expected_type):
        ingredient = Ingredient(type, name, price)

        assert ingredient.get_type()==expected_type