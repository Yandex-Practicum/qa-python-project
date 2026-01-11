from typing import List
from unittest.mock import Mock, patch

import pytest

from practikum.bun import Bun
from practikum.burger import Burger
from practikum.ingredient import Ingredient
from practikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestBurger:

    @patch('practikum.bun.Bun.get_price', return_value=400)
    def test_burger_get_price_with_bun(self, mock_get_price):

        burger = Burger()
        bun = Bun("White bun", 0)
        burger.set_buns(bun)

        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        ingredient2 = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200)

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        actual_price = burger.get_price()

        assert actual_price == 1100

    @pytest.mark.parametrize(
        'sauce,name,price,expected_price',
        [
            ['SAUCE','hot sauce', 200, 400],
            ['FILLING', 'cutlet', 300, 500],
            ['FILLING', 'sausage', 400, 600]
        ]
    )
    def test_burger_get_price_with_ingredients(self,sauce,name,price,expected_price):

        burger = Burger()
        bun = Bun("White bun", 100)
        burger.set_buns(bun)

        ingredient1 = Ingredient(sauce,name,price)
        burger.add_ingredient(ingredient1)

        actual_price = burger.get_price()

        assert actual_price == expected_price

    def test_burger_get_price_with_only_bun(self):
        burger = Burger()
        bun = Bun("White bun", 50)
        burger.set_buns(bun)

        actual_price = burger.get_price()

        assert actual_price == 100

    def test_get_receipt(self):
        burger = Burger()
        bun = Bun("White bun", 100)
        burger.set_buns(bun)

        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        ingredient2 = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200)

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        actual_receipt = burger.get_receipt()

        assert actual_receipt == """(==== White bun ====)
= sauce hot sauce =
= sauce sour cream =
(==== White bun ====)

Price: 500"""




