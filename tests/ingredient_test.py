import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.data import INGREDIENTS_DATA
from tests.conftest import HOT_SAUCE, CUTLET  


class TestIngredient:
    @pytest.mark.parametrize("ingredient_data", INGREDIENTS_DATA)
    def test_ingredient_creation_get_type_returns_correct_type(self, ingredient_data):
        ingredient = Ingredient(
            ingredient_data["type"],
            ingredient_data["name"],
            ingredient_data["price"]
        )
        assert ingredient.get_type() == ingredient_data["type"]

    @pytest.mark.parametrize("ingredient_data", INGREDIENTS_DATA)
    def test_ingredient_creation_get_name_returns_correct_name(self, ingredient_data):
        ingredient = Ingredient(
            ingredient_data["type"],
            ingredient_data["name"],
            ingredient_data["price"]
        )
        assert ingredient.get_name() == ingredient_data["name"]

    @pytest.mark.parametrize("ingredient_data", INGREDIENTS_DATA)
    def test_ingredient_creation_get_price_returns_correct_price(self, ingredient_data):
        ingredient = Ingredient(
            ingredient_data["type"],
            ingredient_data["name"],
            ingredient_data["price"]
        )
        assert ingredient.get_price() == ingredient_data["price"]

    def test_ingredient_sauce_type_constant(self):
        ingredient_type = HOT_SAUCE.get_type()
        assert ingredient_type == INGREDIENT_TYPE_SAUCE

    def test_ingredient_filling_type_constant(self):
        ingredient_type = CUTLET.get_type()
        assert ingredient_type == INGREDIENT_TYPE_FILLING
