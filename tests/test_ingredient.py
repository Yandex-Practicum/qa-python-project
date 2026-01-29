from praktikum.ingredient import Ingredient
from data import NameOfIngridients

class TestIngridient:
    def test_type_ingredient(self):
        type_ingredient = Ingredient(NameOfIngridients.TYPE_ONE, NameOfIngridients.NAME_ONE, NameOfIngridients.PRICE_ONE)
        assert type_ingredient.type == NameOfIngridients.TYPE_ONE

    def test_name_ingredient(self):
        name_ingredient = Ingredient(NameOfIngridients.TYPE_ONE, NameOfIngridients.NAME_ONE, NameOfIngridients.PRICE_ONE)
        assert name_ingredient.name == NameOfIngridients.NAME_ONE

    def test_price_ingredient(self):
        price_ingredient = Ingredient(NameOfIngridients.TYPE_ONE, NameOfIngridients.NAME_ONE, NameOfIngridients.PRICE_ONE)
        assert price_ingredient.price == NameOfIngridients.PRICE_ONE

    def test_get_price(self, space_ingredient):
        assert space_ingredient.get_price() == NameOfIngridients.PRICE_ONE


    def test_get_name(self, space_ingredient):
        assert space_ingredient.get_name() == NameOfIngridients.NAME_ONE

    def test_get_type(self, space_ingredient):
        assert space_ingredient.get_type() == NameOfIngridients.TYPE_ONE