import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestIngredient:

    @pytest.mark.parametrize("create_ingredient", [INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE], indirect=True)
    def test_ingredient_constructor(self, create_ingredient):
        assert isinstance(create_ingredient.type, str) and isinstance(create_ingredient.name, str) and isinstance(create_ingredient.price, float) and create_ingredient.type in [INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE]

    def test_get_ingredient_price(self, create_random_ingredient):
        ingredient = create_random_ingredient()
        assert ingredient.get_price() == ingredient.price

    def test_get_ingredient_name(self, create_random_ingredient):
        ingredient = create_random_ingredient()
        assert ingredient.get_name() == ingredient.name

    def test_get_ingredient_type(self, create_random_ingredient):
        ingredient = create_random_ingredient()
        assert ingredient.get_type() == ingredient.type
