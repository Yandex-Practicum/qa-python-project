import pytest
from data import BunTestData1, BunTestData2
from praktikum.ingredient import Ingredient


class TestIngredient:
    
    @pytest.mark.parametrize('ingredient_type, name, price', [
        (BunTestData1.sauce_type, BunTestData1.sauce_name, BunTestData1.sauce_price),
        (BunTestData1.filling_type, BunTestData1.filling_name, BunTestData1.filling_price),
        (BunTestData2.sauce_type, BunTestData2.sauce_name, BunTestData2.sauce_price),
        (BunTestData2.filling_type, BunTestData2.filling_name, BunTestData2.filling_price)
    ])
    def test_ingredient_constructor_success(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    @pytest.mark.parametrize('ingredient_type, name, price', [
        (BunTestData1.sauce_type, BunTestData1.sauce_name, BunTestData1.sauce_price),
        (BunTestData2.sauce_type, BunTestData2.sauce_name, BunTestData2.sauce_price)
    ])
    def test_get_name_sauce_success(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type, name, price', [
        (BunTestData1.filling_type, BunTestData1.filling_name, BunTestData1.filling_price),
        (BunTestData2.filling_type, BunTestData2.filling_name, BunTestData2.filling_price)
    ])
    def test_get_name_filling_success(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type, name, price', [
        (BunTestData1.sauce_type, BunTestData1.sauce_name, BunTestData1.sauce_price),
        (BunTestData2.sauce_type, BunTestData2.sauce_name, BunTestData2.sauce_price)
    ])
    def test_get_price_sauce_success(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('ingredient_type, name, price', [
        (BunTestData1.filling_type, BunTestData1.filling_name, BunTestData1.filling_price),
        (BunTestData2.filling_type, BunTestData2.filling_name, BunTestData2.filling_price)
    ])
    def test_get_price_filling_success(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('ingredient_type, name, price', [
        (BunTestData1.sauce_type, BunTestData1.sauce_name, BunTestData1.sauce_price),
        (BunTestData2.sauce_type, BunTestData2.sauce_name, BunTestData2.sauce_price)
    ])
    def test_get_type_sauce_success(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize('ingredient_type, name, price', [
        (BunTestData1.filling_type, BunTestData1.filling_name, BunTestData1.filling_price),
        (BunTestData2.filling_type, BunTestData2.filling_name, BunTestData2.filling_price)
    ])
    def test_get_type_filling_success(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        