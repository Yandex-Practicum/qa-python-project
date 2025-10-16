import pytest

from ..database import Database
from ..bun import Bun
from ..ingredient import Ingredient
from ..ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def database():
    return Database()


def test_database_constructor(database):
    """Test Database constructor initializes with buns and ingredients."""
    assert isinstance(database.buns, list)
    assert isinstance(database.ingredients, list)
    assert len(database.buns) == 3
    assert len(database.ingredients) == 6
    
    # Check that buns are properly initialized
    assert isinstance(database.buns[0], Bun)
    assert isinstance(database.buns[1], Bun)
    assert isinstance(database.buns[2], Bun)
    
    # Check that ingredients are properly initialized
    assert isinstance(database.ingredients[0], Ingredient)
    assert isinstance(database.ingredients[1], Ingredient)
    assert isinstance(database.ingredients[2], Ingredient)
    assert isinstance(database.ingredients[3], Ingredient)
    assert isinstance(database.ingredients[4], Ingredient)
    assert isinstance(database.ingredients[5], Ingredient)


def test_database_available_buns(database):
    """Test that available_buns returns the correct list of buns."""
    buns = database.available_buns()
    
    assert isinstance(buns, list)
    assert len(buns) == 3
    
    # Check that all items are Bun instances
    for bun in buns:
        assert isinstance(bun, Bun)
    
    # Check specific bun names and prices
    assert buns[0].get_name() == "black bun"
    assert buns[0].get_price() == 100
    
    assert buns[1].get_name() == "white bun"
    assert buns[1].get_price() == 200
    
    assert buns[2].get_name() == "red bun"
    assert buns[2].get_price() == 300


def test_database_available_ingredients(database):
    """Test available_ingredients returns the correct list of ingredients."""
    ingredients = database.available_ingredients()
    
    assert isinstance(ingredients, list)
    assert len(ingredients) == 6
    
    # Check that all items are Ingredient instances
    for ingredient in ingredients:
        assert isinstance(ingredient, Ingredient)
    
    # Check sauce ingredients
    assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
    assert ingredients[0].get_name() == "hot sauce"
    assert ingredients[0].get_price() == 100
    
    assert ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE
    assert ingredients[1].get_name() == "sour cream"
    assert ingredients[1].get_price() == 200
    
    assert ingredients[2].get_type() == INGREDIENT_TYPE_SAUCE
    assert ingredients[2].get_name() == "chili sauce"
    assert ingredients[2].get_price() == 300
    
    # Check filling ingredients
    assert ingredients[3].get_type() == INGREDIENT_TYPE_FILLING
    assert ingredients[3].get_name() == "cutlet"
    assert ingredients[3].get_price() == 100
    
    assert ingredients[4].get_type() == INGREDIENT_TYPE_FILLING
    assert ingredients[4].get_name() == "dinosaur"
    assert ingredients[4].get_price() == 200
    
    assert ingredients[5].get_type() == INGREDIENT_TYPE_FILLING
    assert ingredients[5].get_name() == "sausage"
    assert ingredients[5].get_price() == 300

