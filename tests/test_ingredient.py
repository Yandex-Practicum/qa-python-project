from conftest import *


class TestIngredient:
    def test_get_name_sauce_success(self, mock_sauce_for_the_first_bun):
        assert mock_sauce_for_the_first_bun.get_name() == Data.SAUCES_NAME

    def test_get_name_filling_success(self, mock_filling_for_the_first_bun):
        assert mock_filling_for_the_first_bun.get_name() == Data.FILLING_NAME

    def test_get_price_sauce_success(self, mock_for_the_second_bun):
        mock_for_the_second_bun.get_price.return_value = Data_1.SAUCES_PRICE
        assert mock_for_the_second_bun.get_price() == Data_1.SAUCES_PRICE

    def test_get_price_filling_success(self, mock_filling_for_the_second_bun):
        mock_filling_for_the_second_bun.get_price.return_value = Data_1.FILLING_PRICE
        assert mock_filling_for_the_second_bun.get_price() == Data_1.FILLING_PRICE

    def test_get_type_sauce_success(self, mock_filling_for_the_first_bun):
        mock_filling_for_the_first_bun.get_type.return_value = Data.SAUCES_TYPE
        assert mock_filling_for_the_first_bun.get_type() == Data.SAUCES_TYPE

    def test_get_type_filling_success(self, mock_filling_for_the_first_bun):
        mock_filling_for_the_first_bun.get_type.return_value = Data.FILLING_TYPE
        assert mock_filling_for_the_first_bun.get_type() == Data.FILLING_TYPE

