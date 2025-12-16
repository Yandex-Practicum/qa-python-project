from unittest.mock import Mock


class Utils:
    @staticmethod
    def mock_bun(bun):
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun[0]
        mock_bun.get_price.return_value = bun[1]
        return mock_bun

    @staticmethod
    def mock_ingredient(ingredient):
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ingredient[0]
        mock_ingredient.get_name.return_value = ingredient[1]
        mock_ingredient.get_price.return_value = ingredient[2]
        return mock_ingredient