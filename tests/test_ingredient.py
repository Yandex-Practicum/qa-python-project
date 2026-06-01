import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngridient:

    @pytest.mark.parametrize("ingredient_type", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "Имя", 100)
        assert ingredient.get_type() == ingredient_type

    
    @pytest.mark.parametrize("name", ["Соус традиционный галактический", "Мясо бессмертных молюсков"])
    def test_get_name(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 100)
        assert ingredient.get_name() == name

    
    @pytest.mark.parametrize("price", [15, 1337])
    def test_get_price(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Имя", price)
        assert ingredient.get_price() == price