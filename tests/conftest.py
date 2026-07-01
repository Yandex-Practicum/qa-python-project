import pytest

from unittest.mock import Mock
from praktikum.burger import Burger


@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def burger_with_three_ingredients(burger):
    ingredient_0 = Mock()
    ingredient_1 = Mock()
    ingredient_2 = Mock()
    
    burger.add_ingredient(ingredient_0)
    burger.add_ingredient(ingredient_1)
    burger.add_ingredient(ingredient_2)
    
    return burger

@pytest.fixture
def burger_with_mocked_bun_and_ingredients(burger):
    mock_bun = Mock()

    mock_ingredient_1 = Mock()
    mock_ingredient_2 = Mock()

    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_1)
    burger.add_ingredient(mock_ingredient_2)

    return burger
