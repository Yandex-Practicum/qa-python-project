from praktikum.ingredient import Ingredient
from data import IngredientData
from praktikum import ingredient_types


class TestIngredient:

    def test_get_price_ingredient(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE,
                                IngredientData.ingredient_name, IngredientData.ingredient_price)
        assert ingredient.get_price() == IngredientData.ingredient_price

    def test_get_name_ingredient(self, set_data_ingredient):
        assert set_data_ingredient.get_name() == IngredientData.ingredient_name

    def test_get_type_ingredient(self, set_data_ingredient):
        assert set_data_ingredient.get_type() == 'FILLING'
