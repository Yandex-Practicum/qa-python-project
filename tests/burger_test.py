from unittest.mock import Mock
import pytest

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        bun = Mock(spec=Bun)
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100

        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Mock(spec=Ingredient)
        ingredient.get_name.return_value = "hot sauce"
        ingredient.get_price.return_value = 100
        ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE

        burger.add_ingredient(ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient1 = Mock(spec=Ingredient)
        ingredient2 = Mock(spec=Ingredient)

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient2

    def test_move_ingredient(self):
        burger = Burger()
        ingredient1 = Mock(spec=Ingredient)
        ingredient2 = Mock(spec=Ingredient)
        ingredient3 = Mock(spec=Ingredient)

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients == [ingredient2, ingredient3, ingredient1]

    @pytest.mark.parametrize(
        "bun_price, ingredients_prices, expected_price",
        [
            (100, [100, 200], 500),   # 100*2 + 100 + 200
            (200, [300], 700),        # 200*2 + 300
            (150, [], 300),           # только булочки
        ]
    )
    def test_get_price(self, bun_price, ingredients_prices, expected_price):
        burger = Burger()

        bun = Mock(spec=Bun)
        bun.get_price.return_value = bun_price
        burger.set_buns(bun)

        for price in ingredients_prices:
            ingredient = Mock(spec=Ingredient)
            ingredient.get_price.return_value = price
            burger.add_ingredient(ingredient)

        assert burger.get_price() == expected_price

    def test_get_receipt(self):
        burger = Burger()

        bun = Mock(spec=Bun)
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100
        burger.set_buns(bun)

        sauce = Mock(spec=Ingredient)
        sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        sauce.get_name.return_value = "hot sauce"
        sauce.get_price.return_value = 100

        filling = Mock(spec=Ingredient)
        filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        filling.get_name.return_value = "cutlet"
        filling.get_price.return_value = 100

        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        receipt = burger.get_receipt()

        assert "(==== black bun ====)" in receipt
        assert "= sauce hot sauce =" in receipt
        assert "= filling cutlet =" in receipt
        assert "Price: 400" in receipt
        