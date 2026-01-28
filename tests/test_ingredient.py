from Diplom_1.ingredient import Ingredient


class TestIngredient:

    def test_ingredient_ingredient_type_true(self):
        ingredient = Ingredient('SAUCE', 'sour cream', 100)
        assert ingredient.type == 'SAUCE'

    def test_ingredient_name_true(self):
        ingr = Ingredient('SAUCE', 'sour sauce', 10)
        assert ingr.name == 'sour sauce'

    def test_ingredient_price_true(self):
        ingr = Ingredient('SAUCE', 'sweet sauce', 20)
        price = ingr.price
        assert price == 20

    def test_ingredient_get_price_true(self):
        ingr = Ingredient('FILLING', 'pork', 20)
        price = ingr.get_price()
        assert ingr.get_price() == 20

    def test_ingredient_get_name_true(self):
        ingr = Ingredient('FILLING', 'pork', 20)
        name = ingr.get_name()
        assert ingr.name == name

    def test_ingredient_get_type_true(self):
        ingr = Ingredient('FILLING', 'pork', 20)
        type = ingr.get_type()
        assert ingr.type == type
