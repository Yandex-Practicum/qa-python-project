import pytest
from unittest.mock import Mock
from tests.data import Credentials

@pytest.fixture
def create_mock_bun():
    """Фикстура возвращает мок булок"""
    def _create_mock_bun(name, price):
        mock_bun = Mock()
        mock_bun.get_name.return_value = name
        mock_bun.get_price.return_value = price
        return mock_bun
    return _create_mock_bun  # возвращаем внутреннюю функцию

@pytest.fixture
def create_mock_ingredient():
    """Фикстура возвращает  моков ингредиентов"""
    def _create_mock_ingredient(type, name, price):
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = type
        mock_ingredient.get_name.return_value = name
        mock_ingredient.get_price.return_value = price
        return mock_ingredient
    return _create_mock_ingredient

