import pytest
from unittest.mock import Mock


@pytest.fixture(params=["SAUCE", "FILLING"])
def mock_ingredient(request):
    type_param = request.param
    mock_ingredient = Mock()
    mock_ingredient.get_price.return_value = 12.99
    mock_ingredient.get_name.return_value = f"test{type_param.lower().capitalize()}"
    mock_ingredient.get_type.return_value = type_param
    return mock_ingredient


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_price.return_value = 99.5
    mock_bun.get_name.return_value = "testBun"
    return mock_bun


@pytest.fixture
def burger():
    from burger import Burger
    return Burger()