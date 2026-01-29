import pytest
from ..ingredient import Ingredient


@pytest.fixture
def ingredient():
    return Ingredient(ingredient_type="sauce", name="Барбекю", price=9.0)


def test_ingredient_creation(ingredient):
    assert ingredient.type == "sauce"
    assert ingredient.name == "Барбекю"
    assert ingredient.price == 9.0

def test_get_price(ingredient):
    assert ingredient.get_price() == 9.0

def test_get_type(ingredient):
    assert ingredient.get_type() == "sauce"

def test_get_name(ingredient):
    assert ingredient.get_name() == "Барбекю"
