import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredients:
    #Получить тип ингредиета
    @pytest.mark.parametrize('ingredient_type, name, price', [[INGREDIENT_TYPE_SAUCE, 'Биокотлета из марсианской Магнолии', 10.11], [INGREDIENT_TYPE_FILLING, 'Соус фирменный Space Sauce', 20.22]])
    def test_getter_return_right_ingrdnt_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
    #Получить наименование ингредиета
    @pytest.mark.parametrize('ingredient_type, name, price', [[INGREDIENT_TYPE_SAUCE, 'Биокотлета из марсианской Магнолии', 10.11], [INGREDIENT_TYPE_FILLING, 'Соус фирменный Space Sauce', 20.22]])
    def test_getter_return_right_ingrdnt_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name
    #Получить цену ингредиета
    @pytest.mark.parametrize('ingredient_type, name, price', [[INGREDIENT_TYPE_SAUCE, 'Биокотлета из марсианской Магнолии', 10.11], [INGREDIENT_TYPE_FILLING, 'Соус фирменный Space Sauce', 20.22]])
    def test_getter_return_right_ingrdnt_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price
