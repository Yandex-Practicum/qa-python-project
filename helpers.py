from unittest.mock import Mock

def create_mock_ingredient(type, name, price):
    """Вспомогательная функция для создания мок-ингредиента."""
    mock = Mock()
    mock.get_type.return_value = type
    mock.get_name.return_value = name
    mock.get_price.return_value = price
    return mock