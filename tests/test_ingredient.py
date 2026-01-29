from praktikum.ingredient import Ingredient
import ingredient_types


class TestIngredient:

    ingredient = Ingredient(
        ingredient_types.INGREDIENT_TYPE_FILLING,
        ingredient_types.INGREDIENT_TYPE_SAUCE,
        ingredient_types.INGREDIENT_PRICE,
    )

    def test_get_price_ingredient(self):

        assert self.ingredient.get_price() == ingredient_types.INGREDIENT_PRICE

    def test_get_name_ingredient(self):

        assert self.ingredient.get_name() == ingredient_types.INGREDIENT_TYPE_SAUCE

    def test_get_type_ingredient(self):

        assert self.ingredient.get_type() == ingredient_types.INGREDIENT_TYPE_FILLING
