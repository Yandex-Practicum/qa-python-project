from unittest.mock import Mock

def create_bun(name="Булочка", price=100):
    bun = Mock()
    bun.get_name.return_value = name
    bun.get_price.return_value = price
    return bun

def create_ingredient(ingredient_type="SAUCE", name="Соус", price=50):
    ingredient = Mock()
    ingredient.get_type.return_value = ingredient_type
    ingredient.get_name.return_value = name
    ingredient.get_price.return_value = price
    return ingredient