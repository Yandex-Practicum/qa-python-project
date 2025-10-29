from praktikum.praktikum import Ingredient


class TestIngredient:

    def test_ingredient_get_name(self):
        ingredient = Ingredient('BUN', 'Соус XX', 50)
        assert ingredient.get_name() == 'Соус XXX'

    def test_ingredient_get_price(self):
        ingredient = Ingredient('BUN', 'Соус XX', 50)
        assert ingredient.get_price() == 75

    def test_ingredient_get_type(self):
        ingredient = Ingredient('BUN', 'Соус XX', 50)
        assert ingredient.get_type() == 'BUN'
