from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING
)

from tests.data.test_data import (
    HOT_SAUCE_NAME,
    HOT_SAUCE_PRICE,
    CUTLET_NAME,
    CUTLET_PRICE,
    SAUSAGE_NAME,
    SAUSAGE_PRICE
)



class TestIngredient:

    def test_ingredient_init(self):
        ingredient = Ingredient(
            INGREDIENT_TYPE_SAUCE,
            HOT_SAUCE_NAME,
            HOT_SAUCE_PRICE
        )

        assert ingredient.type == INGREDIENT_TYPE_SAUCE
        assert ingredient.name == HOT_SAUCE_NAME
        assert ingredient.price == HOT_SAUCE_PRICE

    def test_get_price(self):
        ingredient = Ingredient(
            INGREDIENT_TYPE_FILLING,
            CUTLET_NAME,
            CUTLET_PRICE
        )
        assert ingredient.get_price() == CUTLET_PRICE

    def test_get_name(self):
        ingredient = Ingredient(
            INGREDIENT_TYPE_FILLING,
            SAUSAGE_NAME,
            SAUSAGE_PRICE
        )
        assert ingredient.get_name() == SAUSAGE_NAME

    def test_get_type(self):
        ingredient = Ingredient(
            INGREDIENT_TYPE_SAUCE,
            HOT_SAUCE_NAME,
            HOT_SAUCE_PRICE
        )
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
