from praktikum.ingredient import Ingredient


class TestIngredient:

    def test_ingredient_type(self):
        ingredient = Ingredient('FILLING','Сыр', 15)
        assert ingredient.get_type() == 'FILLING'


    def test_ingredient_name(self):
        ingredient = Ingredient('FILLING','Говяжья котлета', 62)
        assert ingredient.get_name() == 'Говяжья котлета'

    def test_ingredient_price(self):
        ingredient = Ingredient('SAUCE','Кетчуп', 2)
        assert ingredient.get_price() == 2