import pytest

from data import MakeBurger as mb
from ingredient import Ingredient

class TestIngredienr:
    
    def test_init_ingredient_type(self, ingredient_types):
        sauce = ingredient_types(ingredient_types, mb.SAUCE_NAME, mb.SAUCE_PRICE)
        assert sauce.type == ingredient_types
        
    def test_indredient_price(self):
        sause = Ingredient(mb.SAUSE_NAME, mb.SAUSE_PRICE, mb.SAUSE_TYPE)
        assert sause.get_price() == mb.SAUSE_PRICE
    
    def test_ingredient_get_name(self):
        sause = Ingredient(mb.SAUSE_NAME, mb.SAUSE_PRICE, mb.SAUSE_TYPE)
        assert sause.get_name() == mb.SAUSE_NAME
        
    def test_ingredient_type(self):
        sause = Ingredient(mb.SAUSE_NAME, mb.SAUSE_PRICE, mb.SAUSE_TYPE)
        assert sause.get_price() == mb.SAUSE_TYPE   
        