import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


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
    """Фикстура возвращает  мок ингредиентов"""
    def _create_mock_ingredient(type, name, price):
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = type
        mock_ingredient.get_name.return_value = name
        mock_ingredient.get_price.return_value = price
        return mock_ingredient
    return _create_mock_ingredient

@pytest.fixture
def create_mock_burger(create_mock_bun, create_mock_ingredient):
    """Фикстура создает бургер"""
    def _create_mock_burger(bun_name, ingredients_data):
        bun_mock = create_mock_bun(bun_name, 0)
        burger = Burger()
        burger.set_buns(bun_mock)
 
        for ing_type, ing_name in ingredients_data:
            ing_mock = create_mock_ingredient(ing_type, ing_name, 0)
            burger.add_ingredient(ing_mock)
        return burger
    return _create_mock_burger
