from unittest.mock import Mock
from data import Data


class CallMock:

    @staticmethod
    def mock_ingredient():
        mock = Mock()
        mock = mock.Mock()
        mock.get_type.return_value = Data.INGREDIENT_TYPE
        mock.get_name.return_value = Data.INGREDIENT_NAME
        mock.get_price.return_value = Data.INGREDIENT_PRICE
        return mock

    @staticmethod
    def mock_ingredient_2():
        mock = Mock()
        mock = mock.Mock()
        mock.get_type.return_value = Data.INGREDIENT_TYPE_2
        mock.get_name.return_value = Data.INGREDIENT_NAME_2
        mock.get_price.return_value = Data.INGREDIENT_PRICE_2
        return mock

