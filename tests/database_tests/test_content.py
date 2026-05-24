import pytest
from database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabaseContent:
    
    def setup_method(self):
        self.database = Database()
    
    @pytest.mark.parametrize("bun_index, expected_name", [
        (0, "black bun"), (1, "white bun"), (2, "red bun"),
    ])
    def test_bun_has_correct_name(self, bun_index, expected_name):
        assert self.database.buns[bun_index].get_name() == expected_name
    
    @pytest.mark.parametrize("bun_index, expected_price", [
        (0, 100), (1, 200), (2, 300),
    ])
    def test_bun_has_correct_price(self, bun_index, expected_price):
        assert self.database.buns[bun_index].get_price() == expected_price
    
    @pytest.mark.parametrize("ingredient_index, expected_type", [
        (0, INGREDIENT_TYPE_SAUCE), (1, INGREDIENT_TYPE_SAUCE),
        (2, INGREDIENT_TYPE_SAUCE), (3, INGREDIENT_TYPE_FILLING),
        (4, INGREDIENT_TYPE_FILLING), (5, INGREDIENT_TYPE_FILLING),
    ])
    def test_ingredient_has_correct_type(self, ingredient_index, expected_type):
        assert self.database.ingredients[ingredient_index].get_type() == expected_type
    
    @pytest.mark.parametrize("ingredient_index, expected_name", [
        (0, "hot sauce"), (1, "sour cream"), (2, "chili sauce"),
        (3, "cutlet"), (4, "dinosaur"), (5, "sausage"),
    ])
    def test_ingredient_has_correct_name(self, ingredient_index, expected_name):
        assert self.database.ingredients[ingredient_index].get_name() == expected_name
    
    @pytest.mark.parametrize("ingredient_index, expected_price", [
        (0, 100), (1, 200), (2, 300),
        (3, 100), (4, 200), (5, 300),
    ])
    def test_ingredient_has_correct_price(self, ingredient_index, expected_price):
        assert self.database.ingredients[ingredient_index].get_price() == expected_price