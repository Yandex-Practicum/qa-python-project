import pytest
from types import SimpleNamespace
from unittest.mock import Mock

from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    def test_add_ingredient(self, burger_module):
        burger = burger_module.Burger()

        ing1 = SimpleNamespace(get_price=lambda: 10, get_name=lambda: "ing1", get_type=lambda: "X")
        ing2 = SimpleNamespace(get_price=lambda: 20, get_name=lambda: "ing2", get_type=lambda: "Y")
        ing3 = SimpleNamespace(get_price=lambda: 30, get_name=lambda: "ing3", get_type=lambda: "Z")

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        assert [i.get_name() for i in burger.ingredients] == ["ing1", "ing2", "ing3"]

    def test_move_ingredient(self, burger_module):
        burger = burger_module.Burger()

        ing1 = SimpleNamespace(get_price=lambda: 10, get_name=lambda: "ing1", get_type=lambda: "X")
        ing2 = SimpleNamespace(get_price=lambda: 20, get_name=lambda: "ing2", get_type=lambda: "Y")
        ing3 = SimpleNamespace(get_price=lambda: 30, get_name=lambda: "ing3", get_type=lambda: "Z")

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        burger.move_ingredient(2, 0)
        assert [i.get_name() for i in burger.ingredients] == ["ing3", "ing1", "ing2"]

    def test_remove_ingredient(self, burger_module):
        burger = burger_module.Burger()

        ing1 = SimpleNamespace(get_price=lambda: 10, get_name=lambda: "ing1", get_type=lambda: "X")
        ing2 = SimpleNamespace(get_price=lambda: 20, get_name=lambda: "ing2", get_type=lambda: "Y")
        ing3 = SimpleNamespace(get_price=lambda: 30, get_name=lambda: "ing3", get_type=lambda: "Z")

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        burger.remove_ingredient(1)
        assert [i.get_name() for i in burger.ingredients] == ["ing1", "ing3"]

    def test_get_price_with_mocks(self, burger_module):
        burger = burger_module.Burger()

        bun = Mock()
        bun.get_price.return_value = 2.5
        burger.set_buns(bun)

        ing_a = Mock()
        ing_a.get_price.return_value = 1.25

        ing_b = Mock()
        ing_b.get_price.return_value = 3.75

        burger.add_ingredient(ing_a)
        burger.add_ingredient(ing_b)

        # Total = bun*2 + sum(ingredients) = 2.5*2 + 1.25 + 3.75 = 10.0
        assert burger.get_price() == pytest.approx(10.0)

    @pytest.mark.parametrize(
        "bun_name, bun_price, ing_entries, expected_lines",
        [
            (
                "white bun",
                100,
                [
                    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
                    (INGREDIENT_TYPE_FILLING, "cutlet", 100),
                ],
                [
                    "(==== white bun ====)",
                    "= sauce hot sauce =",
                    "= filling cutlet =",
                    "(==== white bun ====)",
                ],
            ),
            (
                "black bun",
                50,
                [],
                [
                    "(==== black bun ====)",
                    "(==== black bun ====)",
                ],
            ),
        ],
    )
    def test_get_receipt_format(self, burger_module, bun_name, bun_price, ing_entries, expected_lines):
        burger = burger_module.Burger()

        bun = Bun(bun_name, bun_price)
        burger.set_buns(bun)

        for t, n, p in ing_entries:
            burger.add_ingredient(Ingredient(t, n, p))

        receipt = burger.get_receipt()
        lines = receipt.splitlines()
        content_lines = [ln for ln in lines if ln.strip()]

        assert content_lines[0] == expected_lines[0]
        assert expected_lines[-1] in content_lines
        for expected in expected_lines[1:-1]:
            assert expected in content_lines

    @pytest.mark.parametrize(
        "bun_name, bun_price, ing_entries, expected_price",
        [
            (
                "white bun",
                100,
                [
                    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
                    (INGREDIENT_TYPE_FILLING, "cutlet", 100),
                ],
                400,  # 2*100 + 100 + 100
            ),
            (
                "black bun",
                50,
                [],
                100,  # 2*50
            ),
        ],
    )
    def test_get_price_from_data(self, burger_module, bun_name, bun_price, ing_entries, expected_price):
        burger = burger_module.Burger()

        bun = Bun(bun_name, bun_price)
        burger.set_buns(bun)

        for t, n, p in ing_entries:
            burger.add_ingredient(Ingredient(t, n, p))

        assert burger.get_price() == expected_price
