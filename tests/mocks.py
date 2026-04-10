from unittest.mock import Mock

def create_mock_bun(name="black bun", price=100):
    bun = Mock()
    bun.get_name.return_value = name
    bun.get_price.return_value = price
    return bun

def create_mock_ingredient(ingredient_type="sauce", name="hot sauce", price=50):
    ing = Mock()
    ing.get_type.return_value = ingredient_type
    ing.get_name.return_value = name
    ing.get_price.return_value = price
    return ing
