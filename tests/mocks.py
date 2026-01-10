from unittest.mock import Mock


class Mocks:
    mock_bun = Mock()
    mock_bun.get_name.return_value = "Булочка с кунжутом"
    mock_bun.get_price.return_value = 2

    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = "Сыр"
    mock_ingredient.get_price.return_value = 30
    mock_ingredient.get_type.return_value = "FILLING"

    mock_sauce = Mock()
    mock_sauce.get_name.return_value = "BBQ"
    mock_sauce.get_price.return_value = 4
    mock_sauce.get_type.return_value = "SAUCE"