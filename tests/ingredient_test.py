from praktikum.ingredient import Ingredient


class TestIngredient:
    def setup_method(self):
        self.ingredient = Ingredient('Начинка', 'Ветчина', 150)

    def test_ingredient_type(self):
        name = self.ingredient.get_type()
        assert name == 'Начинка'

    def test_name(self):
        name = self.ingredient.get_name()
        assert name == 'Ветчина'

    def test_price(self):
        price = self.ingredient.get_price()
        assert price == 150
