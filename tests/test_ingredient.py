import pytest

class TestIngredient:
    def test_ingredient_creation(self, ketchup):
        assert ketchup.type == 'SAUCE'
        assert ketchup.name == 'Кетчуп'
        assert ketchup.price == 3.50

    def test_get_price_ingredient(self, ketchup):
        assert ketchup.get_price() == 3.50

    def test_get_name_ingredient(self, ketchup):
        assert ketchup.get_name() == 'Кетчуп'

    def test_get_type_ingredient(self, cucumber):
        assert cucumber.type == 'FILLING'