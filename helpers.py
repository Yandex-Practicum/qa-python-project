from unittest.mock import Mock

def generate_ingredient_mock(name, price, type):
    ingredient_mock = Mock()
    ingredient_mock.get_price.return_value = price
    ingredient_mock.get_type.return_value = type
    ingredient_mock.get_name.return_value = name
    return ingredient_mock

def generate_bun_mock(price, name = None):
    bun_mock = Mock()
    bun_mock.get_price.return_value = price
    bun_mock.get_name.return_value = name
    return bun_mock
