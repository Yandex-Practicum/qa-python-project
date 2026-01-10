from unittest.mock import Mock

from bun import Bun
from burger import Burger
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        bun = Bun(name="black bun", price=100)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name="hot sauce", price=100)
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, name="cutlet", price=100)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert ingredient not in burger.ingredients

    def test_move_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_FILLING, name="cutlet", price=100)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, name="sausage", price=200)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(index=0, new_index=1)
        assert burger.ingredients[0] == ingredient2
        assert burger.ingredients[1] == ingredient1

    def test_get_price(self):
        burger = Burger()
        bun = Bun(name="black bun", price=100)
        ingredient1 = Ingredient(INGREDIENT_TYPE_FILLING, name="cutlet", price=100)
        ingredient2 = Ingredient(INGREDIENT_TYPE_SAUCE, name="hot sauce", price=50)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        assert burger.get_price() == (100 * 2) + 100 + 50

    def test_get_receipt(self):
        burger = Burger()
        bun = Bun(name="black bun", price=100)
        ingredient1 = Ingredient(INGREDIENT_TYPE_FILLING, name="cutlet", price=100)
        ingredient2 = Ingredient(INGREDIENT_TYPE_SAUCE, name="hot sauce", price=50)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        receipt = burger.get_receipt()
        assert "(==== black bun ====)" in receipt
        assert "= filling cutlet =" in receipt
        assert "= sauce hot sauce =" in receipt
        assert "(==== black bun ====)" in receipt
        assert "Price:" in receipt

    def test_burger_price_with_mocks(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100

        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = 100

        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = 200

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        expected_price = 100 * 2 + 200 + 100
        assert burger.get_price() == expected_price
