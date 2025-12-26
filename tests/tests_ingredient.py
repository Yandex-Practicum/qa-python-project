import pytest
from data import bun_name
from conftest import ingredient_object
from praktikum.bun import Bun


class TestIngredient:

    def test_get_price_350_price_get_price(self, ingredient_object):
        ingredient_object.get_price()
        assert ingredient_object.price == 350.0

    def test_get_name_bbq_get_name(self, ingredient_object):
        ingredient_object.get_name()
        assert ingredient_object.name == 'BBQ'

    def test_get_type_sauce_get_type(self, ingredient_object):
        ingredient_object.get_type()
        assert ingredient_object.type == 'SAUCE'
