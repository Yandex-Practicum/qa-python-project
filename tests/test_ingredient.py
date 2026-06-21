import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:

    # Параметризация включает в себя валидные и граничные значения
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "Sauce Spicy-X", 90),
        (INGREDIENT_TYPE_FILLING, "Beef meteorite", 3000),
        (INGREDIENT_TYPE_SAUCE, "", 0),
        (INGREDIENT_TYPE_FILLING, "", 0)
    ])

    # Проверка что можно задать тип. имя и цену ингридента и данные будут возвращены
    def test_ingredient_get_name_and_get_price_successs(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type and ingredient.get_name() == name and ingredient.get_price() == price

    # Проверяем получение типа ингридиента
    def test_ingredient_get_type_success(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Traditional galaxy sauce", 15)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE