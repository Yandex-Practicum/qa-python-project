import pytest
from praktikum.ingredient import Ingredient
from praktikum.bun import Bun
from unittest.mock import Mock

@pytest.fixture 
def create_ingredient_cutlet():

    cutlet = Ingredient('FILLING', 'cutlet', 200)
    
    return cutlet

@pytest.fixture 
def create_ingredient_sauce():

    sauce = Ingredient('SAUCE', 'hot sauce', 100)
    
    return sauce

@pytest.fixture 
def create_bun():

    bun = Bun("black bun", 100)
    
    return bun


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_price.return_value = 100
    bun.get_name.return_value = "black bun"
    return bun

@pytest.fixture
def mock_ingredient_cutlet():
    cutlet = Mock()

    cutlet.get_type.return_value = "FILLING"
    cutlet.get_name.return_value = "cutlet"
    cutlet.get_price.return_value = 200
    return cutlet

@pytest.fixture
def mock_ingredient_sauce():
    sauce = Mock()

    sauce.get_type.return_value = "SAUCE"
    sauce.get_name.return_value = "hot sauce"
    sauce.get_price.return_value = 100
    return sauce
