import pytest
import praktikum.ingredient_types as ingredient_types
from praktikum.ingredient import Ingredient

class TestIngredient:
    @pytest.mark.parametrize('ingredient_type', [ingredient_types.INGREDIENT_TYPE_SAUCE,
                                                 ingredient_types.INGREDIENT_TYPE_FILLING])
    def test_ingredient_init_is_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type=ingredient_type, name='Test ingredient', price=20)
        assert ingredient.type

    def test_ingredient_init_is_name(self):
        ingredient = Ingredient(ingredient_type=ingredient_types.INGREDIENT_TYPE_SAUCE, name='Test ingredient', price=20)
        assert ingredient.name

    def test_ingredient_init_is_price(self):
        ingredient = Ingredient(ingredient_type='начинка', name='Test ingredient', price=20)
        assert ingredient.price

    @pytest.mark.parametrize('ingredient_type', [ingredient_types.INGREDIENT_TYPE_SAUCE,
                                                 ingredient_types.INGREDIENT_TYPE_FILLING])
    def test_ingredient_get_type_correct(self, ingredient_type):
        ingredient = Ingredient(ingredient_type=ingredient_type, name='Test ingredient', price=20)
        assert ingredient.get_type() == ingredient_type

    def test_ingredient_get_name_correct(self):
        ingredient = Ingredient(ingredient_type='начинка', name='Test ingredient', price=20)
        assert ingredient.get_name() == 'Test ingredient'

    def test_ingredient_get_price_correct(self):
        ingredient = Ingredient(ingredient_type='начинка', name='Test ingredient', price=20)
        assert ingredient.get_price() == 20
