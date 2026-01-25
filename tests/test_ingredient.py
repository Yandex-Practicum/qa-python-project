from praktikum.ingredient import Ingredient
from praktikum import ingredient_types


class TestIngredient:

    def test_get_price(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, 'pyzhak', 1)
        assert ingredient.get_price() == 1

    def test_get_type(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, 'pyzhak', 1)
        assert ingredient.get_type() == ingredient_types.INGREDIENT_TYPE_FILLING

    def test_get_name(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, 'pyzhak', 1)
        assert ingredient.get_name() == 'pyzhak'
