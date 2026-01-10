from unittest.mock import Mock
from practikum.bun import Bun
from practikum.ingredient import Ingredient


def get_mock_bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "blue bun"
    bun.get_price.return_value = 400
    return bun


def get_mock_ingredient_filling():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "dinosaur"
    ingredient.get_price.return_value = 200
    ingredient.get_type.return_value = "FILLING"
    return ingredient


def get_mock_ingredient_sauce():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "sour cream"
    ingredient.get_price.return_value = 50
    ingredient.get_type.return_value = "SAUCE"
    return ingredient
