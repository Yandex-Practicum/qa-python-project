import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:

    @pytest.mark.parametrize('ingredient_type, name, price',
                             [
                                 ['начинка', 'морковь', 12.00],
                                 ['coус', 'сырный', 3.00]
                                 ]
                             )
    def test_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_price() == price

    @pytest.mark.parametrize('ingredient_type, name, price',
                             [
                                 ['начинка', 'лук', 1.00],
                                 ['coус', 'карри', 3.00]
                             ]
                             )
    def test_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type, name, price',
                             [
                                 ['начинка', 'кинза', 2.50],
                                 ['coус', 'болоньезе', 4.00]
                             ]
                             )
    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type



