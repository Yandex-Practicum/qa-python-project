import pytest
from ..bun import Bun
from ..ingredient import Ingredient
from ..burger import Burger


@pytest.fixture
def burger():
    return Burger()
@pytest.fixture
def mock_bun(mocker):
    return mocker.Mock(spec=Bun)
@pytest.fixture
def mock_ingredient(mocker):
    return mocker.Mock(spec=Ingredient)


def test_set_bun_burgers(burger, mock_bun):
    burger.set_buns(mock_bun)

    assert burger.bun == mock_bun


def test_add_ingredient_burgers(burger, mock_ingredient):
    burger.add_ingredient(mock_ingredient)

    assert burger.ingredients[0] == mock_ingredient
    assert len(burger.ingredients) == 1


def test_remove_ingredient_burgers(burger, mock_ingredient):
    burger.add_ingredient(mock_ingredient)
    burger.remove_ingredient(0)

    assert len(burger.ingredients) == 0


def test_move_ingredient_burgers(burger):
    ingredient_1 = Ingredient(name="Чизбургер", ingredient_type="Сыр", price=3.5)
    ingredient_2 = Ingredient(name="Гамбургер", ingredient_type="Котлетка", price=4.6)

    burger.add_ingredient(ingredient_1)
    burger.add_ingredient(ingredient_2)
    burger.move_ingredient(0, 1)

    assert burger.ingredients[0] == ingredient_2
    assert burger.ingredients[1] == ingredient_1


@pytest.mark.parametrize("bun_price, ingredient_prices, expected_price", [
    (1.0, [4.0, 0.5], 6.5),
    (3.0, [0.0], 6.0),
    (3.5, [], 7.0),
])
def test_get_price_burgers(burger, mocker, bun_price, ingredient_prices, expected_price):
    mock_bun = mocker.Mock(spec=Bun)
    mock_bun.get_price.return_value = bun_price
    burger.set_buns(mock_bun)

    for price in ingredient_prices:
        mock_ingredient = mocker.Mock(spec=Ingredient)
        mock_ingredient.get_price.return_value = price
        burger.add_ingredient(mock_ingredient)

    assert burger.get_price() == expected_price


def test_get_receipt_burgers(burger, mock_bun, mock_ingredient):

    mock_bun.get_name.return_value = "Греческая"
    mock_bun.get_price.return_value = 6.0
    mock_ingredient.get_type.return_value = "filling"
    mock_ingredient.get_name.return_value = "Сырочек"
    mock_ingredient.get_price.return_value = 7.5

    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)

    expected_receipt = (
        "(==== Греческая ====)\n"
        "= filling Сырочек =\n"
        "(==== Греческая ====)\n"
        "\nPrice: 19.5"
    )

    assert burger.get_receipt() == expected_receipt