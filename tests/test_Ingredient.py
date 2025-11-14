import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    # Проверить, что присвоен тип ингредиенту
    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            ('SAUCE', 'Соус фирменный Space Sauce', 80),
            ('FILLING', 'Биокотлета из марсианской Магнолии', 424)
        ]
)
    def test_check_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE or INGREDIENT_TYPE_FILLING

    # Проверить, что присвоено имя ингредиенту
    def test_check_get_name_ingredient(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус фирменный Space Sauce', 80)
        assert ingredient.get_name() == 'Соус фирменный Space Sauce'

    # Проверить, что присвоена цена ингредиенту
    def test_check_get_price_ingredient(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус фирменный Space Sauce', 80)
        assert ingredient.get_price() == 80
