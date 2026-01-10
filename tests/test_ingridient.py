import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.mark.parametrize(
    "itype, name, price",
    [
        (INGREDIENT_TYPE_SAUCE, "ketchup", 10),
        (INGREDIENT_TYPE_SAUCE, "chili", 30),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "cheese", 40.5),
    ]
)
class TestIngredient:

    def test_get_type_returns_correct_value(self, itype: str, name: str, price: float):
        ingredient = Ingredient(itype, name, price)
        assert ingredient.get_type() == itype

    def test_get_name_returns_correct_value(self, itype: str, name: str, price: float):
        ingredient = Ingredient(itype, name, price)
        assert ingredient.get_name() == name

    def test_get_price_returns_correct_value(self, itype: str, name: str, price: float):
        ingredient = Ingredient(itype, name, price)
        assert ingredient.get_price() == price
