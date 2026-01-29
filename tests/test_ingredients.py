import pytest

from ..ingredient import Ingredient


class TestIngredient:
    ingredient = pytest.mark.parametrize('ingredient_type, name, price',
                                         [('Соус', 'hot sauce', 1.5)])

    @ingredient
    def test_init_type(self, ingredient_type, name, price):
        assert Ingredient(ingredient_type, name, price).get_type() == ingredient_type

    @ingredient
    def test_init_name(self, ingredient_type, name, price):
        assert Ingredient(ingredient_type, name, price).get_name() == name

    @ingredient
    def test_init_price(self, ingredient_type, name, price):
        assert Ingredient(ingredient_type, name, price).get_price() == price

    @ingredient
    def test_check_type_ingredient_type(self, ingredient_type, name, price):
        assert type(Ingredient(ingredient_type, name, price).get_type()) is str

    @ingredient
    def test_check_name_type(self, ingredient_type, name, price):
        assert type(Ingredient(ingredient_type, name, price).get_name()) is str

    @ingredient
    def test_check_price_type(self, ingredient_type, name, price):
        assert type(Ingredient(ingredient_type, name, price).get_price()) is float


class TestNegativeIngredient:
    ingredient = pytest.mark.parametrize('ingredient_type, name, price',
                                         [(123, None, 0)])

    @ingredient
    def test_check_type_ingredient_type(self, ingredient_type, name, price):
        assert type(Ingredient(ingredient_type, name, price).get_type()) is not str

    @ingredient
    def test_check_name_type(self, ingredient_type, name, price):
        assert type(Ingredient(ingredient_type, name, price).get_name()) is not str

    @ingredient
    def test_check_price_type(self, ingredient_type, name, price):
        assert type(Ingredient(ingredient_type, name, price).get_price()) is not float
