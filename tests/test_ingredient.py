from practikum.ingredient import Ingredient
from practikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestIngredient:

    def test_ingredient_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE,'chili sauce', 300)
        actual_price = ingredient.get_price()

        assert 300 == actual_price

    def test_ingredient_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'chili sauce', 300)
        actual_name = ingredient.get_name()

        assert 'chili sauce' == actual_name

    def test_ingredient_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'chili sauce', 300)
        actual_type = ingredient.get_type()

        assert 'SAUCE' == actual_type

