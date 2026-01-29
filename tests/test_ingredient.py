from Diplom_1.ingredient import Ingredient
from Diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE
from Diplom_1.data import DataForTests


class TestIngredient:

    def test_get_price_successfully(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, DataForTests.CHILI_SAUSE, DataForTests.PRICE_CHILI_SAUSE)
        assert ingredient.get_price() == DataForTests.PRICE_CHILI_SAUSE

    def test_get_name_successfully(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, DataForTests.SOUR_CREAM, DataForTests.PRICE_SOUR_CREAM)
        assert ingredient.get_name() == DataForTests.SOUR_CREAM

    def test_get_type_successfully(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, DataForTests.HOT_SAUSE, DataForTests.PRICE_HOT_SAUSE)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
