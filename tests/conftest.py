import pytest
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from unittest.mock import Mock


@pytest.fixture
def burger():
    burger = Burger()
    return burger

@pytest.fixture
def burger_with_ingredients(burger):
    ingr_1 = Mock()
    ingr_1.name = 'Соус традиционный галактический'
    ingr_1.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ingr_1.get_price.return_value = 15.0

    ingr_2 = Mock()
    ingr_2.name = 'Соус с шипами Антарианского плоскоходца'
    ingr_2.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ingr_2.get_price.return_value = 88.0

    ingr_3 = Mock()
    ingr_3.name = 'Мясо бессмертных моллюсков Protostomia'
    ingr_3.get_type.return_value = INGREDIENT_TYPE_FILLING
    ingr_3.get_price.return_value = 1337.0

    burger.ingredients = [ingr_1, ingr_2, ingr_3]
    return burger

@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = 'Test Bun'
    mock_bun.get_price.return_value = 988.0
    return mock_bun

@pytest.fixture
def mock_sauce():
    mock_sauce = Mock()
    mock_sauce.get_type.return_value = "SAUCE"
    mock_sauce.get_name.return_value = "Spicy-X"
    mock_sauce.get_price.return_value = 90.0
    return mock_sauce

@pytest.fixture
def mock_filling():
    mock_filling = Mock()
    mock_filling.get_type.return_value = "FILLING"
    mock_filling.get_name.return_value = "Protostomia"
    mock_filling.get_price.return_value = 1337.0
    return mock_filling

@pytest.fixture
def mock_ingredient_empty_name():
    mock_bad_ingr = Mock()
    mock_bad_ingr.get_type.return_value = "FILLING"
    mock_bad_ingr.get_name.return_value =""
    mock_bad_ingr.get_price.return_value = 1337.0
    return mock_bad_ingr

@pytest.fixture
def mock_ingredient_negative_price():
    mock_price = Mock()
    mock_price.get_type.return_value = "FILLING"
    mock_price.get_name.return_value = "Bad Ingredient"
    mock_price.get_price.return_value = -10.0
    return mock_price