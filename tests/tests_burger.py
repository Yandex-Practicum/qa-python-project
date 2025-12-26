from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from conftest import burger_object, bun_object, ingredient_object_1, ingredient_object_2, ingredient_object_3
from data import bun_receipt


class TestBurger:

    def test_set_buns_bun_exist_get_attribute(self, burger_object, bun_object):
        burger_object.set_buns(bun_object)
        assert burger_object.bun == bun_object

    def test_set_buns_burger_object_attribute_not_safe(self, burger_object, bun_object):
        burger_object.set_buns(burger_object)
        assert burger_object.bun == burger_object

    def test_add_ingredient_add_ingredient_ingredient_in_list(self, burger_object, ingredient_object_1):
        burger_object.add_ingredient(ingredient_object_1)
        assert ingredient_object_1 in burger_object.ingredients

    def test_remove_ingredient_add_and_remove_ingredient_not_in_list(self, burger_object, ingredient_object_1):
        burger_object.add_ingredient(ingredient_object_1)
        burger_object.remove_ingredient(0)
        assert ingredient_object_1 not in burger_object.ingredients

    def test_move_ingredient_move_ingredient_in_index(self, burger_object, ingredient_object_1, ingredient_object_2,
                                                      ingredient_object_3):
        burger_object.add_ingredient(ingredient_object_1)
        burger_object.add_ingredient(ingredient_object_2)
        burger_object.add_ingredient(ingredient_object_3)
        burger_object.move_ingredient(0, 2)
        assert burger_object.ingredients[1] == ingredient_object_3

    def test_get_price_calculation_amount_get_full_price(self, ingredient_object_1, bun_object, burger_object):
        #burger_object.set_buns(bun_object)
        #burger_object.add_ingredient(ingredient_object_1)
        bun_mock = Mock()
        bun_mock.get_price.return_value = 50
        bun = Bun(bun_mock)

        ingredient_mock = Mock()
        ingredient_mock.get_price.return_value = 100
        ingredient = Ingredient(ingredient_mock)

        assert burger_object.get_price() == 200

    def test_get_receipt(self, burger_object, bun_object, ingredient_object_1):
        burger_object.set_buns(bun_object)
        burger_object.add_ingredient(ingredient_object_1)
        assert burger_object.get_receipt() == bun_receipt
