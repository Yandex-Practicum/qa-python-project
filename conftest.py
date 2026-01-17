import pytest
from unittest.mock import Mock


@pytest.fixture()
def create_mock_burger_prices():
    mock_bun = Mock()
    mock_bun.get_price.return_value = 100
    mock_ingredient_1 = Mock()
    mock_ingredient_1.get_price.return_value = 200
    mock_ingredient_2 = Mock()
    mock_ingredient_2.get_price.return_value = 300
    return mock_bun, mock_ingredient_1, mock_ingredient_2

@pytest.fixture()
def create_mock_burger_names():
    mock_bun = Mock()
    mock_bun.get_name.return_value = 'Булочка с маком'
    mock_ingredient_1 = Mock()
    mock_ingredient_1.get_type.return_value = 'Соус'
    mock_ingredient_1.get_name.return_value = 'Ранч'
    mock_ingredient_2 = Mock()
    mock_ingredient_2.get_type.return_value = 'Начинка'
    mock_ingredient_2.get_name.return_value = 'Котлета'
    return mock_bun, mock_ingredient_1, mock_ingredient_2

