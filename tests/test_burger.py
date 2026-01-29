import pytest
from praktikum.ingredient import Ingredient
from praktikum.bun import Bun
from praktikum.burger import Burger
from unittest.mock import Mock
from praktikum.ingredient_types import *


class TestBurger:
    def test_set_bun_for_burger(self, create_new_bun):
        new_burger = Burger()
        new_burger.set_buns(create_new_bun)
        assert "black bun" in new_burger.get_receipt()

    def test_add_ingredient_for_burger(self, create_new_ingredient):
        ingredients_list = Mock()
        new_burger = Burger()
        new_burger.add_ingredient(create_new_ingredient)
        ingredients_list.get_ingredient_list_len.return_value = 1
        assert ingredients_list.get_ingredient_list_len() == 1

    def test_remove_ingredient_for_burger(self, create_new_bun, create_new_ingredient):
        new_burger = Burger()
        new_burger.set_buns(create_new_bun)
        new_burger.add_ingredient(create_new_ingredient)
        new_burger.remove_ingredient(0)
        assert "hot sauce" not in new_burger.get_receipt()

    def test_move_ingredient_for_burger(self, create_new_ingredient):
        ingredients_list = Mock()
        new_burger = Burger()
        new_burger.add_ingredient(create_new_ingredient)
        create_second_ingredient = Ingredient('FILLING', "cutlet", 100)
        new_burger.add_ingredient(create_second_ingredient)
        ingredients_list.get_ingredient_list.return_value = [create_new_ingredient, create_second_ingredient]
        new_burger.move_ingredient(0,1)
        assert ingredients_list.get_ingredient_list()[0] == create_new_ingredient

    @pytest.mark.parametrize("bun, ingredient1, ingredient2, price",
                             [
                                 (Bun("black bun", 100),
                                  Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
                                  Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
                                  400
                                  ),
                                 (Bun("white bun", 200),
                                  Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
                                  Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
                                  800
                                  ),
                                 (Bun("red bun", 300),
                                  Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300),
                                  Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
                                  1200
                                  ),
                             ])
    def test_get_price_of_burger(self, bun, ingredient1, ingredient2, price):
        new_burger = Burger()
        new_burger.set_buns(bun)
        new_burger.add_ingredient(ingredient1)
        new_burger.add_ingredient(ingredient2)
        assert new_burger.get_price() == price

    def test_get_receipt(self, create_new_bun, create_new_ingredient):
        new_burger = Burger()
        new_burger.set_buns(create_new_bun)
        new_burger.add_ingredient(create_new_ingredient)
        new_filling = Ingredient("FILLING", "cutlet", 100)
        new_burger.add_ingredient(new_filling)
        receipt_string = new_burger.get_receipt()
        new_list = receipt_string.split('\n')
        assert len(new_list) == (5 + 1)