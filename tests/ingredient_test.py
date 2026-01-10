from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
import constants


class TestIngredient:

    def test_get_name(self, ingredient):
        assert ingredient.get_name() == constants.MEAT_SAUCE

    def test_get_type(self, ingredient):
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_get_price(self, ingredient):
        assert ingredient.get_price() == 100

