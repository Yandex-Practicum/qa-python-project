import pytest
from ingredient import Ingredient


class TestIngredient:

    def test_get_type(self):
        ingredient = Ingredient('Начинка', 'Хрустящие минеральные кольца', 300)
        assert ingredient.get_type() == 'Начинка'

    def test_get_name(self):
        ingredient = Ingredient('Начинка', 'Хрустящие минеральные кольца', 300)
        assert ingredient.get_name() == 'Хрустящие минеральные кольца'

    def test_get_price(self):
        ingredient = Ingredient('Начинка', 'Хрустящие минеральные кольца', 300)
        assert ingredient.get_price() == 300