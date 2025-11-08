import pytest

from src.burger import Burger


def test_set_buns_assigns_bun(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun


def test_add_ingredient_appends_to_list(mock_bun, mock_ingredient_sauce):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_sauce)
    assert burger.ingredients == [mock_ingredient_sauce]


def test_remove_ingredient_by_index(mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_sauce)
    burger.add_ingredient(mock_ingredient_filling)

    burger.remove_ingredient(0)
    assert burger.ingredients == [mock_ingredient_filling]


def test_remove_ingredient_invalid_index_raises(mock_bun, mock_ingredient_sauce):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_sauce)

    with pytest.raises(IndexError):
        burger.remove_ingredient(5)


def test_get_receipt_contains_all_parts(mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_sauce)
    burger.add_ingredient(mock_ingredient_filling)

    receipt = burger.get_receipt()

    assert f"(==== {mock_bun.get_name()} ====)" in receipt
    assert "= sauce bbq =" in receipt.lower()
    assert "= filling beef =" in receipt.lower()
    assert f"Price: {burger.get_price()}" in receipt


def test_get_receipt_empty_ingredients(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)
    receipt = burger.get_receipt()

    assert f"(==== {mock_bun.get_name()} ====)" in receipt
    assert "Price:" in receipt
