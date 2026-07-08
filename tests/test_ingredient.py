from ingredient import Ingredient

class TestIngredient:

    def test_get_price_sucsess(self):
        ingredient_type = "INGREDIENT_TYPE_FILLING"
        name = "chicken"
        price = 100.0

        ing = Ingredient(ingredient_type, name, price)
        assert ing.get_price() == price

    def test_get_name_sucsess(self):
        ingredient_type = "INGREDIENT_TYPE_FILLING"
        name = "chicken"
        price = 100.0

        ing = Ingredient(ingredient_type, name, price)
        assert ing.get_name() == name

    def test_get_type_sucsess(self):
        ingredient_type = "INGREDIENT_TYPE_FILLING"
        name = "chicken"
        price = 100.0

        ing = Ingredient(ingredient_type, name, price)
        assert ing.get_type() == ingredient_type