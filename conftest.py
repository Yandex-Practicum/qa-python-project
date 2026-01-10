import pytest
from unittest.mock import Mock


@pytest.fixture
def bun_mock():
    mock = Mock()
    mock.get_name.return_value = "Test Bun"
    mock.get_price.return_value = 10
    return mock

@pytest.fixture
def mock_ingredient():
    def make(ing_type, name, price):
        ing = Mock()
        ing.get_type.return_value = ing_type
        ing.get_name.return_value = name
        ing.get_price.return_value = price
        return ing
    return make
