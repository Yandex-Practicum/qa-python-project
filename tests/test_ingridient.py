import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
import data

class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", data.Ingredients.data_ingredients)
    def test_properties(self,ingredient_type, name, price): #тест_свойств_ингридиентов
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    def test_get_price(self): #тест_метода_get_price
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.get_price() == 100

    def test_ingredient_get_type(self): #тест_метода_get_type
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "cutlet", 100)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_get_name(self): #тест_метода_get_name
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sausage", 300)
        assert ingredient.get_name() == "sausage"