from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredients:

    def test_ingredient_type(self):
        ingredient1 = Ingredient(INGREDIENT_TYPE_FILLING, "Сыр", 3.0)
        ingredient2 = Ingredient(INGREDIENT_TYPE_SAUCE, "Томатный", 2.0)
        assert ingredient1.get_type() == INGREDIENT_TYPE_FILLING
        assert ingredient2.get_type() == INGREDIENT_TYPE_SAUCE

    def test_ingredient_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Горчичный", 2.5)
        assert ingredient.get_price() == 2.5

    def test_ingredient_creation(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Мясо", 5.0)
        assert ingredient.get_name() == "Мясо"
