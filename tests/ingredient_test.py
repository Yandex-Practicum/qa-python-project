from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING



class TestIngredient:

    def test_price_true(self):
        ingredient = Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING,name='Хрустящие минеральные кольца',price=300)
        assert ingredient.get_price() == 300

    def test_name_true(self):
        ingredient = Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING,name='Хрустящие минеральные кольца',price=300)
        assert ingredient.get_name() == 'Хрустящие минеральные кольца'

    def test_type_true(self):
        ingredient = Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE,name='Spicy-X',price=90)
        assert ingredient.get_type() == 'SAUCE'