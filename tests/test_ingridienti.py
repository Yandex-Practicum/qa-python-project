from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


class TestIngredient:

    def test_get_name_correct_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца', 88)
        assert ingredient.get_name() == 'Соус с шипами Антарианского плоскоходца'

    def test_get_price_correct_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'Сыр с астероидной плесенью', 4142)
        assert ingredient.get_price() == 4142

    def test_get_type_correct_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'Сыр с астероидной плесенью', 4142)
        assert ingredient.get_type() == 'FILLING'
