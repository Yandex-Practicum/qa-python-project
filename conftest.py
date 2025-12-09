from unittest.mock import Mock
import pytest
from data import MockBun, MockIngredients


@pytest.fixture(scope='function')
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = MockBun.name
    mock_bun.price = MockBun.price
    return mock_bun


@pytest.fixture(scope='function')
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.name = MockIngredients.name
    mock_ingredient.price = MockIngredients.price
    mock_ingredient.ingredient_type = MockIngredients.ingredient_type

    return mock_ingredient


@pytest.fixture(scope='function')
def mock_two_ingredients(mock_ingredient):
    mock_ingredient_2 = Mock()
    mock_ingredient_2.name = MockIngredients.name_2
    mock_ingredient_2.price = MockIngredients.price_2
    mock_ingredient_2.ingredient_type = MockIngredients.ingredient_type_2
    mock_ingredients = [mock_ingredient, mock_ingredient_2]

    return mock_ingredients