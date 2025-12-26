from unittest.mock import Mock
import pytest
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from generators_data import  generate_random_ingredient_name, generate_random_ingredient_price

@pytest.fixture(scope='function')
def burger():
    burger = Burger()

    mock_ingredient_1 = Mock()
    mock_ingredient_1.type = INGREDIENT_TYPE_FILLING
    mock_ingredient_1.name.return_value = generate_random_ingredient_name()
    mock_ingredient_1.price.return_value = generate_random_ingredient_price()

    mock_ingredient_2 = Mock()
    mock_ingredient_2.type = INGREDIENT_TYPE_SAUCE
    mock_ingredient_2.name.return_value = generate_random_ingredient_name()
    mock_ingredient_2.price.return_value = generate_random_ingredient_price()

    burger.add_ingredient(mock_ingredient_1)
    burger.add_ingredient(mock_ingredient_2)

    return burger