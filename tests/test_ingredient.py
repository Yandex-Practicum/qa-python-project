import pytest
from data import SAUCE_PARAMS, FILLING_PARAMS
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient():
    # проверка получения наименования ингредиента
    @pytest.mark.parametrize('ingredient, params', [['sauce', SAUCE_PARAMS],
                                                    ['filling', FILLING_PARAMS]])
    def test_remove_ingredient(self, ingredient, params, request):
        ingredient_fixture = request.getfixturevalue(ingredient)
        ingredient_name = ingredient_fixture.get_name() # получаем наименование ингредиента
        assert ingredient_name == params['name'] and type(ingredient_name) == str# проверяем соответствие наименования ингредиента

    # проверка получения цены ингредиента
    @pytest.mark.parametrize('ingredient, params', [['sauce', SAUCE_PARAMS],
                                                    ['filling', FILLING_PARAMS]])
    def test_get_price(self, ingredient, params, request):
        ingredient_fixture = request.getfixturevalue(ingredient)
        ingredient_price = ingredient_fixture.get_price()#получаем цену ингредиента
        assert ingredient_price == params['price'] #проверяем соответствие цены ингредиента

    # проверка получения типа ингредиента
    @pytest.mark.parametrize('ingredient, params, type_i', [['sauce', SAUCE_PARAMS, INGREDIENT_TYPE_SAUCE],
                                                          ['filling', FILLING_PARAMS, INGREDIENT_TYPE_FILLING]])
    def test_get_type(self, ingredient, params, type_i, request):
        ingredient_fixture = request.getfixturevalue(ingredient)
        ingredient_price = ingredient_fixture.get_type() #получаем тип ингредиента
        assert ingredient_price == type_i  and type(ingredient_price) == str #проверяем соответствие типа ингредиента


