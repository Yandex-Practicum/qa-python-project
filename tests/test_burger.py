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


def test_add_ingredient():
    burger = Burger()
    ing = MagicMock()
    ing.get_price.return_value = 30.0
    burger.add_ingredient(ing)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] is ing

@pytest.mark.parametrize(
    "index_to_remove, expected_len",
    [
        (0, 2),   
        (1, 2),   
        (2, 2),  
    ],
)
def test_remove_ingredient_valid_cases(index_to_remove, expected_len):
    burger = Burger()
    ings = [MagicMock(), MagicMock(), MagicMock()]
    for i, ing in enumerate(ings):
        ing.get_type.return_value = f"type_{i}"
        ing.get_name.return_value = f"name_{i}"
        ing.get_price.return_value = i * 10
        burger.add_ingredient(ing)

    burger.remove_ingredient(index_to_remove)
    
    assert len(burger.ingredients) == expected_len
    removed_item = ings[index_to_remove]
    assert removed_item not in burger.ingredients

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
    ings = []
    prices = [10.0, 20.0, 30.0]
    for i in range(3):
        ing = MagicMock()
        ing.get_price.return_value = prices[i]
        burger.add_ingredient(ing)
        ings.append(ing)

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
    burger.add_ingredient(ing)

    receipt = burger.get_receipt()
    lines = receipt.splitlines()

    assert lines[0] == "(==== Classic Bun ====)"
    assert "Spicy Sauce" in lines[1]
    assert lines[-1].startswith("Price: ")
