from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


class TestIngredient:

    # тест на получение названия ингредиента
    def test_get_name_true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.get_name() == "hot sauce"

    # тест на получение стоимости ингредиента
    def test_get_price_true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.get_price() == 100

    # тест на получение типа ингредиента
    def test_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
