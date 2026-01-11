from unittest.mock import Mock
from data import TestData
from praktikum import ingredient_types


class BurgerMock:

    @staticmethod
    def mock_bun():
        mock_bun = Mock()
        mock_bun.get_name.return_value = TestData.BUN_NAME_VALID_BLACK
        mock_bun.get_price.return_value = TestData.BUN_PRICE_VALID
        return mock_bun

    @staticmethod
    def mock_bun_with_price(price):
        mock_bun = Mock()
        mock_bun.get_name.return_value = TestData.BUN_NAME_VALID_BLACK
        mock_bun.get_price.return_value = price
        return mock_bun

    @staticmethod
    def mock_ingredient():
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ingredient_types.INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = TestData.SAUCE_NAME_SOUR
        mock_ingredient.get_price.return_value = TestData.INGREDIENT_PRICE_VALID
        return mock_ingredient

    @staticmethod
    def mock_ingredient_with_parameters(ingredient_type, name, price):
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ingredient_type
        mock_ingredient.get_name.return_value = name
        mock_ingredient.get_price.return_value = price
        return mock_ingredient

    @staticmethod
    def mock_ingredient_with_price(price):
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ingredient_types.INGREDIENT_TYPE_FILLING
        mock_ingredient.get_name.return_value = TestData.FILLING_NAME_SAUSAGE
        mock_ingredient.get_price.return_value = price
        return mock_ingredient

