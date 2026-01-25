import pytest

from data.ingredients import ingredients, buns
from data.mock import mock_bun, mock_ingredient1, mock_ingredient2
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestBurger:
    @pytest.mark.parametrize('bun_data', buns)
    def test_burger_set_buns(self, bun_data):
        burger = Burger()
        name, price = bun_data
        bun = Bun(name, price)
        burger.set_buns(bun)
        assert burger.bun.get_name() == name
        assert burger.bun.get_price() == price

    @pytest.mark.parametrize('ingredient_data', ingredients)
    def test_burger_add_ingredient(self, ingredient_data):
        burger = Burger()
        ingredient_type, name, price = ingredient_data
        ingredient = Ingredient(ingredient_type, name, price)
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_burger_add_same_ingredient_twice(self):
        burger = Burger()
        ingredient = Ingredient(*ingredients[0])

        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient, ingredient]

    def test_burger_add_different_ingredients(self):
        burger = Burger()

        for i in range(5):
            ingredient = Ingredient(*ingredients[i])
            burger.add_ingredient(ingredient)

        assert len(burger.ingredients) == 5

    @pytest.mark.parametrize('ingredient_data', ingredients)
    def test_burger_remove_ingredient(self, ingredient_data):
        burger = Burger()
        ingredient_type, name, price = ingredient_data
        ingredient = Ingredient(ingredient_type, name, price)

        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_burger_move_ingredient(self):
        burger = Burger()

        ingredient1 = Ingredient(*ingredients[0])
        ingredient2 = Ingredient(*ingredients[1])
        ingredient3 = Ingredient(*ingredients[2])
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients == [ingredient2, ingredient3, ingredient1]

    def test_burger_get_price_with_bun_and_ingredients(self):
        burger = Burger()

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        expected_price = mock_bun.get_price() * 2 + mock_ingredient1.get_price() + mock_ingredient2.get_price()

        assert burger.get_price() == expected_price

    def test_burger_get_price_with_only_bun(self):
        burger = Burger()

        burger.set_buns(mock_bun)

        expected_price = mock_bun.get_price() * 2

        assert burger.get_price() == expected_price

    def test_burger_receipt_with_bun_and_ingredients(self):
        burger = Burger()

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        expected_receipt = (
            f"(==== {mock_bun.get_name()} ====)\n"
            f"= {mock_ingredient1.get_type().lower()} {mock_ingredient1.get_name()} =\n"
            f"= {mock_ingredient2.get_type().lower()} {mock_ingredient2.get_name()} =\n"
            f"(==== {mock_bun.get_name()} ====)\n\n"
            f"Price: {mock_bun.get_price() * 2 + mock_ingredient1.get_price() + mock_ingredient2.get_price()}"
        )

        assert burger.get_receipt() == expected_receipt

    def test_burger_receipt_with_only_bun(self):
        burger = Burger()
        burger.set_buns(mock_bun)

        expected_receipt = (
            f"(==== {mock_bun.get_name()} ====)\n"
            f"(==== {mock_bun.get_name()} ====)\n\n"
            f"Price: {mock_bun.get_price() * 2}"
        )

        assert burger.get_receipt() == expected_receipt
