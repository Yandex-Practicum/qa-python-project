from praktikum.ingredient import Ingredient

class TestIngredient:

    def test_ingredient_get_name_returns_correct_name(self):
        ingredient = Ingredient('SAUCE', 'Соус с шипами Антарианского плоскоходца', 88)
        assert ingredient.get_name() == 'Соус с шипами Антарианского плоскоходца'

    def test_ingredient_get_price_returns_correct_price(self):
        ingredient = Ingredient('SAUCE', 'Соус с шипами Антарианского плоскоходца', 88)
        assert ingredient.get_price() == 88

    def test_ingredient_get_type_returns_correct_type(self):
        ingredient = Ingredient('SAUCE', 'Соус с шипами Антарианского плоскоходца', 88)
        assert ingredient.get_type() == 'SAUCE'