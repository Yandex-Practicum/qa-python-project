from unittest.mock import Mock

def make_mock_bun(name="Sesame Bun", price=3.0):
    bun = Mock()
    bun.get_name.return_value = name
    bun.get_price.return_value = price
    return bun

def make_mock_ingredient(name="Lettuce", ing_type="Vegetable", price=1.2):
    ing = Mock()
    ing.get_name.return_value = name
    ing.get_type.return_value = ing_type
    ing.get_price.return_value = price
    return ing