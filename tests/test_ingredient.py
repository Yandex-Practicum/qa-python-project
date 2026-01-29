from praktikum.ingredient import Ingredient

class TestIngredient:

    def test_get_price_of_ingredient(self, ingredient_filling):
        ingredient = Ingredient(ingredient_filling[0], ingredient_filling[1], ingredient_filling[2])
        assert ingredient.get_price() == ingredient_filling[2]

    def test_get_name_of_ingredient(self, ingredient_sous):
        ingredient = Ingredient(ingredient_sous[0], ingredient_sous[1], ingredient_sous[2])
        assert ingredient.get_name() == ingredient_sous[1]

    def test_get_type_of_ingredient(self, ingredient_sous):
        ingredient = Ingredient(ingredient_sous[0], ingredient_sous[1], ingredient_sous[2])
        assert ingredient.get_type() == ingredient_sous[0]
