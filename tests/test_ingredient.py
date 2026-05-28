from data import SAUCE_TYPE, SAUCE_NAME, SAUCE_PRICE

def test_ingredient_get_name(ingredient):
     assert ingredient.get_name() == SAUCE_NAME


def test_ingredient_get_price(ingredient):
    assert ingredient.get_price() == SAUCE_PRICE


def test_ingredient_get_type(ingredient):
    assert ingredient.get_type() == SAUCE_TYPE