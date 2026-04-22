from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    def test_init_ingredient_valid_type_true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.type == INGREDIENT_TYPE_SAUCE
       

    def test_init_ingredient_valid_name_true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.name == "hot sauce"

    def test_init_ingredient_valid_price_true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.price == 100

    def test_get_price_valid_ingredient_returns_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)

        assert ingredient.get_price() == 150

    def test_get_name_valid_ingredient_returns_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 50)

        assert ingredient.get_name() == "sour cream"

    def test_get_type_valid_ingredient_returns_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200)

        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING