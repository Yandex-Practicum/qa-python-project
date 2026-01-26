import pytest
from Diplom_1.burger import Ingredient

class TestIngredient:
    @pytest.fixture
    def setup(self):
        ingredient = Ingredient(ingredient_type="FILLING", name="Test Ingredient", price=2.0)
        return ingredient

    def test_get_name(self, setup):
        ingredient = setup
        assert ingredient.get_name() == "Test Ingredient"

    def test_get_price(self, setup):
        ingredient = setup
        assert ingredient.get_price() == 2.0

    def test_get_type(self, setup):
        ingredient = setup
        assert ingredient.get_type() == "FILLING"

    def test_ingredient_initialization(self, setup):
        ingredient = setup
        assert ingredient.type == "FILLING" and ingredient.name == "Test Ingredient" and ingredient.price == 2.0