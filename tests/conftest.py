import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture
def mock_bun_data(spec=Bun):
    mock = Mock()
    mock.get_name.return_value = "Ржаная"
    mock.get_price.return_value = 150
    return mock

@pytest.fixture
def mock_ingredient_data(spec=Ingredient):
    mock = Mock()
    mock.get_type.return_value = "начинка"
    mock.get_name.return_value = "Котлета"
    mock.get_price.return_value = 250
    return mock