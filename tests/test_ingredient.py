from praktikum.ingredient import Ingredient


class TestBurger:

    def test_ingredient_initialization_price(self):
        ingredient = Ingredient('SAUCE', 'Острый соус чилли', 100)
        assert ingredient.get_price() == 100

    def test_ingredient_initialization_type(self):
        ingredient = Ingredient('SAUCE', 'Острый соус чилли', 100)
        assert ingredient.get_type() == 'SAUCE'

    def test_ingredient_initialization_name(self):
        ingredient = Ingredient('SAUCE', 'Острый соус чилли', 100)
        assert ingredient.get_name() == 'Острый соус чилли'

