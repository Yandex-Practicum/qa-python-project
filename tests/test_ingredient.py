from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE

class TestIngredient:

    def test_get_price(self, ingredient):
        assert ingredient.get_price() == 10

    def test_get_name(self, ingredient):
        assert ingredient.get_name() == 'hot sauce'

    def test_get_type(self, ingredient):
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
