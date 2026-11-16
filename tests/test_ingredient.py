import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    @pytest.mark.parametrize("ing_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90),
        (INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков Protostomia", 1337),
        (INGREDIENT_TYPE_FILLING, "Сыр", 50),
    ])
    def test_ingredient_getters(self, ing_type, name, price):
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.get_type() == ing_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price