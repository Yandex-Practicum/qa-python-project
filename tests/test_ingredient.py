from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE

class TestIngredient:
    def test_init(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'some_name', 2.5)
        assert ingredient.type == INGREDIENT_TYPE_SAUCE
        assert ingredient.name == 'some_name'
        assert ingredient.price == 2.5

    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'some_name', 2.5)
        assert ingredient.get_price() == 2.5

    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'some_name', 2.5)
        assert ingredient.get_name() == 'some_name'

    def test_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'some_name', 2.5)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE