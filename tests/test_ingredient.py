from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


def test_get_price():
    bulka = Ingredient(INGREDIENT_TYPE_SAUCE, 'Rufl', 100)
    price = bulka.get_price()
    assert 100 == price


#
def test_get_name():
    bulka = Ingredient(INGREDIENT_TYPE_SAUCE, 'Rufl', 100)
    name = bulka.get_name()
    assert 'Rufl' == name


def test_get_type():
    bulka = Ingredient(INGREDIENT_TYPE_SAUCE, 'Rufl', 100)
    type = bulka.get_type()
    assert 'SAUCE' == type
