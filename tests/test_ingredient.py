import pytest

from .. ingredient import Ingredient
from .. ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.mark.parametrize("ingredient_type,name,price", [
    (INGREDIENT_TYPE_FILLING, "cheese", 25.0),
    (INGREDIENT_TYPE_SAUCE, "ketchup", 10.0),
])
def test_ingredient_creation(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    
    assert ingredient.get_type() == ingredient_type
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price
    assert isinstance(ingredient.get_name(), str)
    assert isinstance(ingredient.get_price(), float)
    assert isinstance(ingredient.get_type(), str)



# @pytest.fixture
# def filling_ingredient():
#     return Ingredient(
#         ingredient_type=INGREDIENT_TYPE_FILLING,
#         name="cheese",
#         price=25.0
#     )


# @pytest.fixture
# def sauce_ingredient():
#     return Ingredient(
#         ingredient_type=INGREDIENT_TYPE_SAUCE,
#         name="ketchup",
#         price=10.0
#     )


# def test_ingredient_get_name(ingredient):
#     assert ingredient.get_name() == 'very_cool'
#     assert isinstance(ingredient.get_name, str)


# def test_ingredient_get_price(ingredient):
#     assert ingredient.get_price() == 25.0
#     assert isinstance(ingredient.get_price, float)


# def test_ingredient_type(filling_ingredient, sauce_ingredient):
#     assert filling_ingredient. get_type == INGREDIENT_TYPE_FILLING
#     assert sauce_ingredient.get_type == INGREDIENT_TYPE_SAUCE
#     assert isinstance(filling_ingredient.get_type, str) and isinstance(sauce_ingredient.get_type, str) 
    