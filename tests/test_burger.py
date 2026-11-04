import pytest
from unittest.mock import MagicMock
from burger import Burger


@pytest.fixture
def mock_bun():
    bun = MagicMock()
    bun.get_name.return_value = "Classic Bun"
    bun.get_price.return_value = 50.0
    return bun


def test_set_buns(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)
    assert burger.bun is mock_bun


def test_add_ingredient_adds_to_list():
    burger = Burger()
    ing = MagicMock()
    burger.add_ingredient(ing)
    assert len(burger.ingredients) == 1


def test_add_ingredient_stores_same_object():
    burger = Burger()
    ing = MagicMock()
    burger.add_ingredient(ing)
    assert burger.ingredients[0] is ing


@pytest.mark.parametrize("index_to_remove", [0, 1, 2])
def test_remove_ingredient_reduces_count(index_to_remove):
    burger = Burger()
    for _ in range(3):
        burger.add_ingredient(MagicMock())
    burger.remove_ingredient(index_to_remove)
    assert len(burger.ingredients) == 2


@pytest.mark.parametrize("index_to_remove", [0, 1, 2])
def test_remove_ingredient_deletes_right_item(index_to_remove):
    burger = Burger()
    ings = [MagicMock(), MagicMock(), MagicMock()]
    for ing in ings:
        burger.add_ingredient(ing)
    burger.remove_ingredient(index_to_remove)
    assert ings[index_to_remove] not in burger.ingredients


def test_remove_ingredient_invalid():
    burger = Burger()
    burger.add_ingredient(MagicMock())
    with pytest.raises(IndexError):
        burger.remove_ingredient(5)


@pytest.mark.parametrize(
    "from_idx, to_idx, expected_prices_order",
    [
        (0, 1, [20.0, 10.0, 30.0]),
        (2, 0, [30.0, 10.0, 20.0]),
        (1, 1, [10.0, 20.0, 30.0]),
    ],
)
def test_move_ingredient_cases(from_idx, to_idx, expected_prices_order):
    burger = Burger()
    prices = [10.0, 20.0, 30.0]
    for price in prices:
        ing = MagicMock()
        ing.get_price.return_value = price
        burger.add_ingredient(ing)

    burger.move_ingredient(from_idx, to_idx)

    result_prices = [ing.get_price() for ing in burger.ingredients]
    assert result_prices == expected_prices_order


def test_get_price(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)

    ing1 = MagicMock()
    ing1.get_price.return_value = 20.0
    ing2 = MagicMock()
    ing2.get_price.return_value = 40.0

    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)

    price = burger.get_price()
    expected = (mock_bun.get_price.return_value * 2) + 20.0 + 40.0
    assert price == expected

def test_get_receipt(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)

    ing = MagicMock()
    ing.get_type.return_value = "sauce"
    ing.get_name.return_value = "Spicy Sauce"
    ing.get_price.return_value = 20.0
    burger.add_ingredient(ing)

    expected_receipt = (
        "(==== Classic Bun ====)\n"
        "= sauce Spicy Sauce =\n"
        "(==== Classic Bun ====)\n"
        "\n"
        "Price: 120.0"
    )

    assert burger.get_receipt() == expected_receipt
