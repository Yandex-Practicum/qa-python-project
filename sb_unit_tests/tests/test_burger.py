from typing import List
from unittest.mock import Mock

import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING,
)


@pytest.fixture
def burger() -> Burger:
    return Burger()


def test_set_buns_and_add_ingredients_price_with_mocks(burger: Burger):
    bun = Mock(spec=Bun)
    bun.get_price.return_value = 100
    burger.set_buns(bun)

    ing1 = Mock(spec=Ingredient)
    ing1.get_price.return_value = 25
    ing2 = Mock(spec=Ingredient)
    ing2.get_price.return_value = 75

    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)

    assert burger.get_price() == 100 * 2 + 25 + 75


@pytest.mark.parametrize(
    "initial, move_from, move_to, expected",
    [
        (["a", "b", "c"], 0, 2, ["b", "c", "a"]),
        (["a", "b", "c", "d"], 3, 1, ["a", "d", "b", "c"]),
    ],
)
def test_move_ingredient_reorders_list(burger: Burger, initial: List[str], move_from: int, move_to: int, expected: List[str]):
    burger.set_buns(Bun("stub", 1))
    burger.ingredients = initial.copy()  # type: ignore[assignment]
    burger.move_ingredient(move_from, move_to)
    assert burger.ingredients == expected


def test_remove_ingredient_removes_correct_item(burger: Burger):
    burger.set_buns(Bun("stub", 1))
    burger.ingredients = ["x", "y", "z"]  # type: ignore[assignment]
    burger.remove_ingredient(1)
    assert burger.ingredients == ["x", "z"]


def test_get_receipt_format_and_values():
    bun = Bun("white bun", 200)
    ing1 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
    ing2 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)

    b = Burger()
    b.set_buns(bun)
    b.add_ingredient(ing1)
    b.add_ingredient(ing2)

    receipt_lines = [line for line in b.get_receipt().splitlines() if line.strip()]

    assert receipt_lines[0] == f"(==== {bun.get_name()} ====)"
    assert receipt_lines[-2] == f"(==== {bun.get_name()} ====)"

    assert f"= sauce {ing1.get_name()} =" in receipt_lines
    assert f"= filling {ing2.get_name()} =" in receipt_lines

    assert receipt_lines[-1] == f"Price: {b.get_price()}"
