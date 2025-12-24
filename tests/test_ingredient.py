from praktikum.ingredient import Ingredient


class TestIngredient:

    def test_ingredient_get_name(self):
        ingredient = Ingredient('SAUCE', 'Соус Экстратеррестрис', 3000)
        assert ingredient.get_name() == 'Соус Экстратеррестрис', 'Unable to get ingredient name'

    def test_ingredient_get_price(self):
        ingredient = Ingredient('SAUCE', 'Соус Экстратеррестрис', 3000)
        assert ingredient.get_price() == 3000, 'Unable to get ingredient price'

    def test_ingredient_get_type(self):
        ingredient = Ingredient('SAUCE', 'Соус Экстратеррестрис', 3000)
        assert ingredient.get_type() == 'SAUCE', 'Unable to get ingredient type'
