import pytest

from Diplom_1.praktikum.ingredient import Ingredient
from Diplom_1.data import INGREDIENT_DATA

class TestIngredient:

    @pytest.mark.parametrize('price', [25, 0, 9999999.99, 0.01])
    def test_get_price(self, price):
        ingredient = Ingredient(INGREDIENT_DATA.get('type'), INGREDIENT_DATA.get('name'), price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('name', ['Острый чили', '', 'Фэнси органик соус без глютена, лактозы, сахара, короче масло'])
    def test_get_name(self, name):
        ingredient = Ingredient(INGREDIENT_DATA.get('type'), name, INGREDIENT_DATA.get('price'))
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type', ['острый', '', 'Не содержит продукты животного происхождения'])
    def test_get_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, INGREDIENT_DATA.get('name'), INGREDIENT_DATA.get('price'))
        assert ingredient.get_type() == ingredient_type