from unittest.mock import Mock

import pytest

from praktikum.burger import Burger


class TestBurgerInit:
    def test_initial_state(self):
        burger = Burger()

        assert burger.bun is None
        assert burger.ingredients == []

    def test_ingredients_not_shared_between_instances(self):
        burger1 = Burger()
        burger2 = Burger()

        burger1.add_ingredient(Mock())

        assert burger2.ingredients == []


class TestSetBuns:
    def test_set_buns_assigns_bun(self, bun_mock):
        burger = Burger()

        burger.set_buns(bun_mock)

        assert burger.bun is bun_mock

    def test_set_buns_overwrites_previous(self, bun_mock):
        burger = Burger()
        old_bun = Mock()

        burger.set_buns(old_bun)
        burger.set_buns(bun_mock)

        assert burger.bun is bun_mock


class TestAddIngredient:
    def test_add_single_ingredient(self, ingredient_mock):
        burger = Burger()

        burger.add_ingredient(ingredient_mock)

        assert burger.ingredients == [ingredient_mock]

    def test_add_multiple_preserves_order(self):
        burger = Burger()
        ingredients = [Mock(), Mock(), Mock()]

        for ing in ingredients:
            burger.add_ingredient(ing)

        assert burger.ingredients == ingredients


class TestRemoveIngredient:
    @pytest.mark.parametrize(
        "index, expected_order",
        [(0, [1, 2]), (1, [0, 2]), (2, [0, 1])],
        ids=["first", "middle", "last"],
    )
    def test_remove_by_index(self, index, expected_order):
        burger = Burger()
        ingredients = [Mock(), Mock(), Mock()]
        for ing in ingredients:
            burger.add_ingredient(ing)

        burger.remove_ingredient(index)

        assert burger.ingredients == [ingredients[i] for i in expected_order]

    def test_remove_invalid_index_raises(self):
        burger = Burger()

        with pytest.raises(IndexError):
            burger.remove_ingredient(0)


class TestMoveIngredient:
    @pytest.mark.parametrize(
        "from_index, to_index, expected_order",
        [
            (0, 2, [1, 2, 0]),
            (2, 0, [2, 0, 1]),
            (1, 1, [0, 1, 2]),
            (0, 1, [1, 0, 2]),
        ],
        ids=["forward", "backward", "same_position", "adjacent"],
    )
    def test_move_ingredient(self, from_index, to_index, expected_order):
        burger = Burger()
        ingredients = [Mock(), Mock(), Mock()]
        for ing in ingredients:
            burger.add_ingredient(ing)

        burger.move_ingredient(from_index, to_index)

        assert burger.ingredients == [ingredients[i] for i in expected_order]

    def test_move_invalid_index_raises(self):
        burger = Burger()

        with pytest.raises(IndexError):
            burger.move_ingredient(0, 5)


class TestGetPrice:
    def test_price_bun_only(self, burger_with_bun):
        assert burger_with_bun.get_price() == pytest.approx(200.0)

    def test_price_bun_and_ingredients(self, burger_with_bun):
        for price in (30.0, 20.0, 50.0):
            ing = Mock()
            ing.get_price.return_value = price
            burger_with_bun.add_ingredient(ing)

        assert burger_with_bun.get_price() == pytest.approx(300.0)

    @pytest.mark.parametrize(
        "bun_price, ingredient_prices, expected",
        [
            (0, [], 0),
            (100, [], 200),
            (100, [50], 250),
            (99.99, [0.01], 199.99),
        ],
        ids=["zero", "bun_only", "one_ingredient", "floats"],
    )
    def test_price_parametrized(self, bun_price, ingredient_prices, expected):
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = bun_price
        burger.set_buns(bun)
        for price in ingredient_prices:
            ing = Mock()
            ing.get_price.return_value = price
            burger.add_ingredient(ing)

        assert burger.get_price() == pytest.approx(expected)


class TestGetReceipt:
    def test_receipt_without_ingredients(self, burger_with_bun):
        receipt = burger_with_bun.get_receipt()

        expected = (
            "(==== black bun ====)\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 200.0"
        )
        assert receipt == expected

    def test_receipt_with_ingredients(self, burger_with_bun):
        filling = Mock()
        filling.get_type.return_value = "FILLING"
        filling.get_name.return_value = "cutlet"
        filling.get_price.return_value = 100.0

        sauce = Mock()
        sauce.get_type.return_value = "SAUCE"
        sauce.get_name.return_value = "hot sauce"
        sauce.get_price.return_value = 100.0

        burger_with_bun.add_ingredient(filling)
        burger_with_bun.add_ingredient(sauce)

        receipt = burger_with_bun.get_receipt()

        expected = (
            "(==== black bun ====)\n"
            "= filling cutlet =\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 400.0"
        )
        assert receipt == expected