import pytest
import praktikum.ingredient_types

from unittest.mock import Mock
from praktikum.burger import Burger

@pytest.fixture
def cooked_burger():
    burger = Burger()
    mock_bun = Mock()
    mock_bun.get_name.return_value = "brioche"
    mock_bun.get_price.return_value = 10.0

    mock_filling = Mock()
    mock_filling.get_name.return_value = "cheese"
    mock_filling.get_type.return_value = praktikum.ingredient_types.INGREDIENT_TYPE_FILLING
    mock_filling.get_price.return_value = 5

    mock_sauce = Mock()
    mock_sauce.get_name.return_value = "ketchunes"
    mock_sauce.get_type.return_value = praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE
    mock_sauce.get_price.return_value = 15

    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_filling)
    burger.add_ingredient(mock_sauce)

    return burger
