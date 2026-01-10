from praktikum.ingredient import Ingredient
from data import Data


class TestIngredient:
    def test_type_and_name_and_price_of_ingredient_true(self):
        ingredient = Ingredient(ingredient_type=Data.ingredient.get('type'),
                                name=Data.ingredient.get('name'),
                                price=Data.ingredient.get('price'))
        assert (ingredient.type == Data.ingredient.get('type') and
                ingredient.name == Data.ingredient.get('name') and
                ingredient.price == Data.ingredient.get('price'))

    def test_get_price_return_right_price(self, awesome_ingredient):
        assert awesome_ingredient.get_price() == awesome_ingredient.price

    def test_get_name_return_right_name(self, awesome_ingredient):
        assert awesome_ingredient.get_name() == awesome_ingredient.name

    def test_get_type_return_right_type(self, awesome_ingredient):
        assert awesome_ingredient.get_type() == awesome_ingredient.type
