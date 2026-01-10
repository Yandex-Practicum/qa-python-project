import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:

    def test_type_ingredient(self):
        ingredient = Ingredient('Соус', 'Огненный', 40.3)

        assert ingredient.get_type() == 'Соус'

    def test_name_ingredient(self):
        ingredient = Ingredient('Соус', 'Огненный', 40.3)

        assert ingredient.get_name() == 'Огненный'

    def test_price_ingredient(self):
        ingredient = Ingredient('Соус', 'Огненный', 40.3)

        assert ingredient.get_price() == 40.3
