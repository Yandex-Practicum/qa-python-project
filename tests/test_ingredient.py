from praktikum.ingredient import Ingredient


def test_ingredient_get_price():
    assert Ingredient('test_ingredient', 'test_name', 3).get_price() == 3

def test_ingredient_get_name():
    assert Ingredient('test_ingredient', 'test_name', 3).get_name() == "test_name"

def test_ingredient_get_type():
     assert Ingredient('test_ingredient', 'test_name', 3).get_type() == "test_ingredient"