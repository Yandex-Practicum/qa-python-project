from praktikum.ingredient import Ingredient


class TestIngredient:

    def test_get_price(self):
        ingredient = Ingredient('соус', 'гарнир', 10)
        assert ingredient.get_price() == 10

    def test_get_name(self):
        ingredient = Ingredient('соус', 'гарнир', 10)
        assert ingredient.get_name() == 'гарнир'

    def test_get_type(self):
        ingredient = Ingredient('соус', 'гарнир', 10)
        assert ingredient.get_type() == 'соус'