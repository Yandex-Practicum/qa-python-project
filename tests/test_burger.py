import pytest
from Diplom_1.burger import Burger
from Diplom_1.ingredient import Ingredient
from Diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_set_buns(bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_remove_ingredient_removes_correct(self, mock_ingredient):
        burger = Burger()
        ing_1 = mock_ingredient(INGREDIENT_TYPE_FILLING, "sause", 1.0)
        ing_2 = mock_ingredient(INGREDIENT_TYPE_FILLING, "salad", 2.0)
        burger.add_ingredient(ing_1)
        burger.add_ingredient(ing_2)
        burger.remove_ingredient(0)
        assert burger.ingredients[0] == ing_2
        assert len(burger.ingredients) == 1

    def test_move_ingredient_moves(self, mock_ingredient):
        burger = Burger()
        ing_1 = mock_ingredient(INGREDIENT_TYPE_FILLING, "A", 1.0)
        ing_2 = mock_ingredient(INGREDIENT_TYPE_FILLING, "B", 2.0)
        ing_3 = mock_ingredient(INGREDIENT_TYPE_FILLING, "C", 3.0)

        burger.add_ingredient(ing_1)
        burger.add_ingredient(ing_2)
        burger.add_ingredient(ing_3)

        burger.move_ingredient(2, 0)

        assert burger.ingredients[0] == ing_3
        assert burger.ingredients[1] == ing_1
        assert burger.ingredients[2] == ing_2

    def test_get_price(self, bun_mock, mock_ingredient):
        burger = Burger()
        burger.set_buns(bun_mock)
        ing_1 = mock_ingredient(INGREDIENT_TYPE_FILLING, "beef", 3.0)
        ing_2 = mock_ingredient(INGREDIENT_TYPE_SAUCE, "sauce", 1.0)

        burger.add_ingredient(ing_1)
        burger.add_ingredient(ing_2)

        expected_price = bun_mock.get_price() * 2 + ing_1.get_price() + ing_2.get_price()
        assert burger.get_price() == expected_price

    def test_get_receipt(self, bun_mock, mock_ingredient):
        burger = Burger()
        burger.set_buns(bun_mock)

        ing_1 = mock_ingredient(INGREDIENT_TYPE_FILLING, "Meat", 3.0)
        ing_2 = mock_ingredient(INGREDIENT_TYPE_SAUCE, "Mayonnaise", 1.0)

        burger.add_ingredient(ing_1)
        burger.add_ingredient(ing_2)

        expected_receipt = '\n'.join([
            f"(==== {bun_mock.get_name()} ====)",
            f"= filling Meat =",
            f"= sauce Mayonnaise =",
            f"(==== {bun_mock.get_name()} ====)\n",
            f"Price: {burger.get_price()}"
        ])

        actual_receipt = burger.get_receipt()
        assert actual_receipt == expected_receipt

    def test_get_price_raises_if_bun_not_set(self):
        burger = Burger()
        with pytest.raises(AttributeError):
            burger.get_price()
