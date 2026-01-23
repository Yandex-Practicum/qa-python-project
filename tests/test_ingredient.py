from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING

DATA_INGREDIENT = [INGREDIENT_TYPE_FILLING, 'cheese', 100]


class TestIngredient:

    def test_get_price(self):
        ingredient = Ingredient(*DATA_INGREDIENT)

        assert DATA_INGREDIENT[2] == ingredient.get_price()

    def test_get_name(self):
        ingredient = Ingredient(*DATA_INGREDIENT)

        assert DATA_INGREDIENT[1] == ingredient.get_name()

    def test_get_type(self):
        ingredient = Ingredient(*DATA_INGREDIENT)

        assert DATA_INGREDIENT[0] == ingredient.get_type()
