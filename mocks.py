from unittest.mock import Mock

import data


# Мокируем булку
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = data.bun[0]
    mock_bun.get_price.return_value = data.bun[1]
    return mock_bun

# Мокируем ингредиент
def mock_ingredient(ingredient_type, name, price):
    mock_ingredient = Mock()
    mock_ingredient.get_type.return_value = ingredient_type
    mock_ingredient.get_name.return_value = name
    mock_ingredient.get_price.return_value = price
    return mock_ingredient
