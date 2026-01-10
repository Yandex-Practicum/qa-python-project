import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:
    @pytest.fixture(params=[
        ("начинка", "сыр", 100),
        ("соус", "кетчуп", 50),
    ])
    def ingredient(self, request):
        return Ingredient(*request.param)

    def test_constructor(self, ingredient):
        assert ingredient.type == ingredient.type
        assert ingredient.name == ingredient.name
        assert ingredient.price == ingredient.price

    def test_get_price_successfully_get(self, ingredient):
        assert ingredient.get_price() == ingredient.price

    def test_get_name_successfully_get(self, ingredient):
        assert ingredient.get_name() == ingredient.name

    def test_get_type_successfully_get(self, ingredient):
        assert ingredient.get_type() == ingredient.type
