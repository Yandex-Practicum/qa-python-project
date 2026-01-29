from helper import *
from data import *

class TestIngredient:

    def test_get_name_sauce_success(self, mock_sauce):
        expected_name = mock_sauce.get_name()
        sauce_names = get_sauce_names()
        assert expected_name in sauce_names

    def test_get_name_filling_success(self, mock_filling):
        expected_name = mock_filling.get_name()
        filling_names = get_filling_names()
        assert expected_name in filling_names

    def test_get_price_sauce_success(self, mock_sauce):
        expected_price = mock_sauce.get_price()
        sauce_prices = get_sauce_prices()
        assert expected_price in sauce_prices

    def test_get_price_filling_success(self, mock_filling):
        expected_price = mock_filling.get_price()
        filling_prices = get_filling_prices()
        assert expected_price in filling_prices

    def test_get_type_sauce_success(self, mock_sauce):
        expected_type = mock_sauce.get_type()
        assert expected_type == INGREDIENT_TYPE_SAUCE

    def test_get_type_filling_success(self, mock_filling):
        expected_type = mock_filling.get_type()
        assert expected_type == INGREDIENT_TYPE_FILLING