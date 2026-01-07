import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    @pytest.mark.parametrize("ingredient_type,name,price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100.0),
        (INGREDIENT_TYPE_SAUCE, "cheese sauce", 150.5),
        (INGREDIENT_TYPE_FILLING, "salad", 30.0),
    ])
    def test_ingredient_initialization_and_getters(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    def test_ingredient_types(self):
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 50.0)
        filling = Ingredient(INGREDIENT_TYPE_FILLING, "bacon", 120.0)
        assert sauce.get_type() == "SAUCE"
        assert filling.get_type() == "FILLING"

    def test_get_price_returns_correct_value(self):
        """Проверка получения цены для конкретного ингредиента"""
        price = 45.0
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "mayonnaise", price)
        assert ingredient.get_price() == price

    def test_ingredient_prices_can_be_summed(self):
        """Проверка, что цены ингредиентов можно складывать (они численного типа)"""
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "mayonnaise", 45.0)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, "lettuce", 30.0)

        assert ingredient1.get_price() + ingredient2.get_price() == 75.0

