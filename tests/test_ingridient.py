import pytest

from praktikum.ingredient import Ingredient

class TestIngredient:

    @pytest.mark.parametrize("ingredient_type,name,price", [
        ("соус", "сырный", 100.0),
        ("начинка", "говяжья", 200.0),
    ])
    def test_ingredient_initialization(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    def test_get_price(self):
        ingredient = Ingredient("соус", "сырный", 100)
        assert ingredient.get_price() == 100

    def test_get_name(self):
        ingredient = Ingredient("соус", "сырный", 100)
        assert ingredient.get_name() == "сырный"

    def test_get_type(self):
        ingredient = Ingredient("соус", "сырный", 100)
        assert ingredient.get_type() == "соус"