import pytest
from unittest.mock import Mock
from pages.bun import Bun
from pages.ingredient import Ingredient


@pytest.fixture
def mock_bun():
    def _mock_bun(name="mock bun", price=100):
        mock = Mock(spec=Bun)
        mock.get_name.return_value = name
        mock.get_price.return_value = price
        return mock
    return _mock_bun


@pytest.fixture
def mock_ingredient():
    def _mock_ingredient(ingredient_type="FILLING", name="mock ingredient", price=100):
        mock = Mock(spec=Ingredient)
        mock.get_type.return_value = ingredient_type
        mock.get_name.return_value = name
        mock.get_price.return_value = price
        return mock
    return _mock_ingredient