import pytest
from ingredient import Ingredient


class TestIngridient:
    def test_get_price(self):
        ing = Ingredient('SAUCE', "hot sauce", 100)
        assert ing.get_price() == 100

    def test_get_name(self):
        ing = Ingredient('FILLING', "dinosaur", 200)
        assert ing.get_name() == "dinosaur"

    def test_get_type(self):
        ing = Ingredient('FILLING', "cutlet", 100)
        assert ing.get_type() == 'FILLING'
