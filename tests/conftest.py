import pytest
from unittest.mock import Mock

from praktikum.burger import Burger


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = 'crater bun'
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def mock_ingredients():
    filling_meteorite = Mock()
    filling_meteorite.get_price.return_value = 3000
    filling_meteorite.get_name.return_value = 'beef meteorite'
    filling_meteorite.get_type.return_value = 'FILLING'

    sauce_galactic = Mock()
    sauce_galactic.get_price.return_value = 15
    sauce_galactic.get_name.return_value = 'galactic sauce'
    sauce_galactic.get_type.return_value = 'SAUCE'

    filling_salad = Mock()
    filling_salad.get_price.return_value = 4400
    filling_salad.get_name.return_value = 'exo-plantago salad'
    filling_salad.get_type.return_value = 'FILLING'

    filling_cheese = Mock()
    filling_cheese.get_price.return_value = 4142
    filling_cheese.get_name.return_value = 'asteroid mold cheese'
    filling_cheese.get_type.return_value = 'FILLING'

    return [filling_meteorite, sauce_galactic, filling_salad, filling_cheese]


@pytest.fixture
def mock_bun_full():
    bun = Mock()
    bun.get_name.return_value = 'fluorescent bun'
    bun.get_price.return_value = 988
    return bun


@pytest.fixture
def burger_with_ingredients(burger, mock_ingredients):
    for ingredient in mock_ingredients:
        burger.add_ingredient(ingredient)
    return burger
