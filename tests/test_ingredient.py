from ingredient import Ingredient

class TestIngredientMethods:

    def test_ingredient_type_true(self):
        ingredient = Ingredient("SAUCE", None,None)
        assert ingredient.type == "SAUCE"

    def test_ingredient_name_true(self):
        ingredient = Ingredient(None, "hot sauce",None)
        assert ingredient.name == "hot sauce"


    def test_ingredient_price_true(self):
        ingredient = Ingredient(None, None,150)
        assert ingredient.price == 150


    def test_ingredient_get_price_true(self):
        ingredient = Ingredient(None, None, 150)
        assert ingredient.get_price() == 150

    def test_ingredient_get_name_true(self):
        ingredient = Ingredient(None, "hot sauce", None)
        assert ingredient.get_name() == "hot sauce"

    def test_ingredient_get_type_true(self):
        ingredient = Ingredient("SAUCE", None, None)
        assert ingredient.get_type() == "SAUCE"