# Названия и цены булочек
BUN_NAME_1 = "Test Bun 1"
BUN_NAME_2 = "Test Bun 2"
BUN_PRICE = 50

# Названия и цены ингредиентов
SAUCE_NAME = "Test Sauce"
FILLING_NAME = "Test Filling"
SAUCE_PRICE = 20
FILLING_PRICE = 40

def create_mock_ingredient(name, price):
    from unittest.mock import Mock
    from praktikum.ingredient import Ingredient
    mock = Mock(spec=Ingredient)
    mock.get_name.return_value = name
    mock.get_price.return_value = price
    return mock
