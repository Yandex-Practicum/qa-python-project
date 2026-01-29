from praktikum.ingredient import Ingredient
import data as data


class TestIngredient:

    def test_get_price_ingredient(self):
        ingredient = Ingredient(data.ingredients[2][0], data.ingredients[2][1], data.ingredients[2][2])
        assert ingredient.get_price() == data.ingredients[2][2]

    def test_get_name_ingredient(self):
        ingredient = Ingredient(data.ingredients[1][0], data.ingredients[1][1], data.ingredients[1][2])
        assert ingredient.get_name() == data.ingredients[1][1]

    def test_get_type_ingredient(self):
        ingredient = Ingredient(data.ingredients[0][0], data.ingredients[0][1], data.ingredients[0][2])
        assert ingredient.get_type() == data.ingredients[0][0]