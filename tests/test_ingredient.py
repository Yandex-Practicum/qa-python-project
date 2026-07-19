from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    def test_ingredient_creation(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0)
        assert ingredient.type == INGREDIENT_TYPE_SAUCE
        assert ingredient.name == "hot sauce"
        assert ingredient.price == 100.0

    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150.0)
        assert ingredient.get_price() == 150.0

    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200.0)
        assert ingredient.get_name() == "sour cream"

    def test_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200.0)
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING