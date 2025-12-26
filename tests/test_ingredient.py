import pytest
from praktikum.ingredient import Ingredient

class TestIngredient:
    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            ("filling", "cheese", 150),
            ("filling", "cutlet", 300),
            ("sauce", "ketchup", 50),
            ("sauce", "mustard", 50)
        ]
    )
    def test_ingredient_price(self, ingredient_type, name, price):
        assert Ingredient(ingredient_type, name, price).get_price() == price


    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            ("filling", "cheese", 150),
            ("filling", "cutlet", 300),
            ("sauce", "ketchup", 50),
            ("sauce", "mustard", 50)
        ]
    )
    def test_ingredient_name(self, ingredient_type, name, price):
        assert Ingredient(ingredient_type, name, price).get_name() == name


    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            ("filling", "cheese", 150),
            ("filling", "cutlet", 300),
            ("sauce", "ketchup", 50),
            ("sauce", "mustard", 50)
        ]
    )
    def test_ingredient_type(self, ingredient_type, name, price):
        assert Ingredient(ingredient_type, name, price).get_type() == ingredient_type
