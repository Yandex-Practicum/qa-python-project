import pytest

from praktikum.burger import Burger


def test_set_buns_sets_bun(burger, bun):
    burger.set_buns(bun)
    assert burger.bun == bun


@pytest.mark.parametrize("count", [1, 2, 3])
def test_add_ingredient_appends_to_list(burger, ingredient_sauce, count):
    for _ in range(count):
        burger.add_ingredient(ingredient_sauce)
    assert len(burger.ingredients) == count
    assert burger.ingredients[-1] == ingredient_sauce


def test_remove_ingredient_deletes_by_index(burger, ingredient_sauce, ingredient_filling):
    burger.add_ingredient(ingredient_sauce)
    burger.add_ingredient(ingredient_filling)

    burger.remove_ingredient(0)

    assert burger.ingredients == [ingredient_filling]


def test_move_ingredient_changes_order(burger, ingredient_sauce, ingredient_filling):
    burger.add_ingredient(ingredient_sauce)
    burger.add_ingredient(ingredient_filling)

    burger.move_ingredient(0, 1)

    assert burger.ingredients == [ingredient_filling, ingredient_sauce]


def test_get_price_counts_bun_twice_and_ingredients(burger, bun, ingredient_sauce, ingredient_filling):
    burger.set_buns(bun)
    burger.add_ingredient(ingredient_sauce)
    burger.add_ingredient(ingredient_filling)

    assert burger.get_price() == 100 * 2 + 50 + 200
    bun.get_price.assert_called()
    ingredient_sauce.get_price.assert_called()
    ingredient_filling.get_price.assert_called()


def test_get_price_with_no_ingredients(burger, bun):
    burger.set_buns(bun)
    assert burger.get_price() == 100 * 2


def test_get_receipt_format_and_content(burger, bun, ingredient_sauce, ingredient_filling):
    burger.set_buns(bun)
    burger.add_ingredient(ingredient_sauce)
    burger.add_ingredient(ingredient_filling)

    receipt = burger.get_receipt()

    assert f"(==== {bun.get_name()} ====)" in receipt
    assert f"(==== {bun.get_name()} ====)\n" in receipt
    assert f"= sauce {ingredient_sauce.get_name()} =" in receipt
    assert f"= filling {ingredient_filling.get_name()} =" in receipt
    assert f"Price: {burger.get_price()}" in receipt