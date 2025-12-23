from Prakticum.ingredient import Ingredient
import pytest
from Prakticum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestIngredient:

    @pytest.fixture
    def ingredient(self):
        return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)

    def test_get_price(self, ingredient):
        assert ingredient.get_price() == 100

    def test_get_name(self, ingredient):
        assert ingredient.get_name() == "hot sauce"

    def test_get_type(self, ingredient):
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
