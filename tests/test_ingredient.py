from info import InfoBun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE

class TestIngredient():
    def test_get_price(self):
        price = 10
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, InfoBun.INGREDIENT_BACON, price)
        assert ingredient.get_price() == price
    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, InfoBun.INGREDIENT_CUTLETE, 9)
        assert ingredient.get_name() == InfoBun.INGREDIENT_CUTLETE
    def test_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, InfoBun. INGRIDIET_FISH, 11)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
