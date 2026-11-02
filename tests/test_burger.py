import pytest

from burger import Burger
from bun import Bun
from ingredient import Ingredient
from unittest.mock import MagicMock


class TestBurger:

    def test_init(self):
        burger = Burger()

        assert burger.bun is None
        assert burger.ingredients == []

    def test_adding_bun(self):
        burger = Burger()
        bun = Bun('black bun', 10)
        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient('black bun', 'cheeseburger', 10)
        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]

    @pytest.mark.parametrize(
        "index, expected_names",
        [
            (0, ["cheese"]),
            (1, ["tomato"]),
        ],
    )
    def test_remove_ingredient(self, add_burger, index, expected_names):
        add_burger.remove_ingredient(index)

        assert [i.get_name() for i in add_burger.ingredients] == expected_names

    def test_move_ingredient(self, add_burger):
        add_burger.move_ingredient(0, 1)

        assert add_burger.ingredients[0].get_name() == 'cheese'
        assert add_burger.ingredients[1].get_name() == 'tomato'

    @pytest.mark.parametrize(
        "ingredients, expected_price",
        [
            ([], 20),
            ([("vegetable", "tomato", 6), ("dairy", "cheese", 6)], 32),
        ],
    )
    def test_get_price(self, ingredients, expected_price):
        burger = Burger()
        burger.set_buns(Bun("black bun", 10))
        for ing_type, name, price in ingredients:
            burger.add_ingredient(Ingredient(ing_type, name, price))

        assert burger.get_price() == expected_price

    def test_get_price_with_mocked_bun(self):
        burger = Burger()
        mock_bun = MagicMock()
        mock_bun.get_price.return_value = 5
        burger.set_buns(mock_bun)

        assert burger.get_price() == 10

    def test_get_receipt(self, add_burger):
        receipt = add_burger.get_receipt()

        assert '(==== black bun ====)' in receipt
        assert '= vegetable tomato =' in receipt
        assert '= dairy cheese =' in receipt
        assert 'Price: 32' in receipt