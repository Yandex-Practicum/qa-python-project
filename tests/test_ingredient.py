import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, expected_type", [
    (Ingredient(INGREDIENT_TYPE_SAUCE, "Гургунзола", 60), INGREDIENT_TYPE_SAUCE),
    (Ingredient(INGREDIENT_TYPE_FILLING, "Нестабильная энергия Цефеида", 150), INGREDIENT_TYPE_FILLING)
                                                                ]
                            )
    def test_get_type(self, ingredient_type, expected_type):
        assert ingredient_type.get_type() == expected_type

    def test_get_name(self, ingredient):
        assert ingredient.get_name() == "Кольца j1407b"

    def test_get_price(self, ingredient):
        assert ingredient.get_price() == 280