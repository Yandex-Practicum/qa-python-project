from praktikum.ingredient import Ingredient
class TestIngredient:
    ingredient = Ingredient('FILLING','Говяжий метеорит (отбивная)', 3000)
    def test_ingredient_initialization(self):
        assert self.ingredient.type == 'FILLING' and self.ingredient.name == 'Говяжий метеорит (отбивная)' and self.ingredient.price == 3000
    def test_get_price_retuns_price(self):
        assert self.ingredient.get_price() == 3000
    def test_get_name_retuns_name(self):
        assert self.ingredient.get_name() == 'Говяжий метеорит (отбивная)'
    def test_get_type_retuns_type(self):
        assert self.ingredient.get_type() == 'FILLING'
