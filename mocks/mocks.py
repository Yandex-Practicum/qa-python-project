from unittest.mock import Mock

class Mocks:
    mock_bun = Mock()
    mock_bun.get_name.return_value = 'black bun'
    mock_bun.get_price.return_value = 100

    mock_ingredient_souce = Mock()
    mock_ingredient_souce.get_name.return_value = 'hot sauce'
    mock_ingredient_souce.get_price.return_value = 100
    mock_ingredient_souce.get_type.return_value = 'SAUCE'

    mock_ingredient_filling = Mock()
    mock_ingredient_filling.get_name.return_value = 'cutlet'
    mock_ingredient_filling.get_price.return_value = 100
    mock_ingredient_filling.get_type.return_value = 'FILLING'