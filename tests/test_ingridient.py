from DATA import Ingridients, Price
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


def test_ingredient_initialization_type(mock_ingredient):
    assert mock_ingredient.type == INGREDIENT_TYPE_SAUCE


def test_ingredient_initialization_name(mock_ingredient):
    assert mock_ingredient.name == Ingridients.HOT_SAUCE


def test_ingredient_initialization_price(mock_ingredient):
    assert mock_ingredient.price == Price.HOT_SAUCE


def test_ingredient_get_price(mock_ingredient):
    actual_price = mock_ingredient.get_price()
    expected_price = Price.HOT_SAUCE
    assert actual_price == expected_price


def test_ingredient_get_name(mock_ingredient):
    actual_name = mock_ingredient.get_name()
    expected_name = Ingridients.HOT_SAUCE
    assert actual_name == expected_name


def test_ingredient_get_type(mock_ingredient):
    actual_type = mock_ingredient.get_type()
    expected_type = INGREDIENT_TYPE_SAUCE
    assert actual_type == expected_type
