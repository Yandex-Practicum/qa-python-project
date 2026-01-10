import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestIngredient:

    #Создание ингредиента.
    def test_create_ingredient(self, filling):
        assert filling.get_price() == 170
        assert filling.get_name() == 'potato'
        assert filling.get_type() == INGREDIENT_TYPE_FILLING

    #Получение стоимости ингредиента.
    def test_get_price_ingredient(self, filling):
        assert filling.get_price() == 170

    #Получение наименования ингредиента.
    def test_get_name_ingredient(self, filling):
        assert filling.get_name() == 'potato'

    # Получение типа ингредиента.
    @pytest.mark.parametrize(
        'types, name, price, result',
        [
            [INGREDIENT_TYPE_SAUCE, 'cheese', 160, 'SAUCE'],
            [INGREDIENT_TYPE_FILLING, 'potato', 170, 'FILLING']
        ]
    )
    def test_get_type_correct_type(self, types, name, price, result):
        ingredient = Ingredient(types, name, price)
        assert ingredient.get_type() == result

