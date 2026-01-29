from data import DataIngredient
from praktikum.ingredient import Ingredient


class TestIngredient:

    def test_get_price_check_the_price(self):
        name, price, type_ingredient = DataIngredient.get_data_ingredient()
        ingredient = Ingredient(ingredient_type=type_ingredient, name=name, price=price)
        assert ingredient.get_price() == price

    def test_get_name_check_the_name(self):
        name, price, type_ingredient = DataIngredient.get_data_ingredient()
        ingredient = Ingredient(ingredient_type=type_ingredient, name=name, price=price)
        assert ingredient.get_name() == name

    def test_get_type_check_the_type(self):
        name, price, type_ingredient = DataIngredient.get_data_ingredient()
        ingredient = Ingredient(ingredient_type=type_ingredient, name=name, price=price)
        assert ingredient.get_type() == type_ingredient
