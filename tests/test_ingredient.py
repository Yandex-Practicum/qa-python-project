import pytest
from praktikum.database import Database


class TestIngredient:
    @pytest.mark.parametrize('ingredient_type_by_index', [0, 3])
    def test_ingredient_init_is_type(self, ingredient_type_by_index):
        db = Database()
        ingredient = db.ingredients[ingredient_type_by_index]
        assert ingredient.type

    def test_ingredient_init_is_name(self):
        db = Database()
        ingredient = db.ingredients[0]
        assert ingredient.name

    def test_ingredient_init_is_price(self):
        db = Database()
        ingredient = db.ingredients[0]
        assert ingredient.price

    @pytest.mark.parametrize('ingredient_type_by_index', [0, 3])
    def test_ingredient_get_type_correct(self, ingredient_type_by_index):
        db = Database()
        ingredient = db.ingredients[ingredient_type_by_index]
        assert ingredient.get_type() == ingredient.type

    def test_ingredient_get_name_correct(self):
        db = Database()
        ingredient = db.ingredients[0]
        assert ingredient.get_name() == ingredient.name

    def test_ingredient_get_price_correct(self):
        db = Database()
        ingredient = db.ingredients[0]
        assert ingredient.get_price() == ingredient.price
