import pytest
from ..praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    """Тестируем получение цены ингредиента"""
    @pytest.mark.parametrize('ingredient_fixture', ['sauce_ingredient', 'filling_ingredient'])
    def test_get_ingredient_price_positive(self, request, ingredient_fixture):
        ingredient = request.getfixturevalue(ingredient_fixture)
        assert ingredient.get_price() == 100

    """Тестируем получение названия ингредиента"""
    @pytest.mark.parametrize('ingredient_fixture, expected', [
        ('sauce_ingredient', 'hot sauce'),
        ('filling_ingredient', 'cutlet')
    ])
    def test_get_ingredient_name_positive(self, request, ingredient_fixture, expected):
        ingredient = request.getfixturevalue(ingredient_fixture)
        assert ingredient.get_name() == expected

    """Тестируем получение типа ингредиента"""
    @pytest.mark.parametrize('ingredient_fixture, expected', [
        ('sauce_ingredient', INGREDIENT_TYPE_SAUCE),
        ('filling_ingredient', INGREDIENT_TYPE_FILLING)
    ])
    def test_get_ingredient_type_positive(self, request, ingredient_fixture, expected):
        ingredient = request.getfixturevalue(ingredient_fixture)
        assert ingredient.get_type() == expected
