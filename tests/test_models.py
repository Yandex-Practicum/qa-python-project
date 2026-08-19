import pytest

from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.mark.parametrize(
    "name,price",
    [
        ("sesame bun", 45.0),
        ("plain bun", 80.5),
    ],
)
def test_bun_get_name_returns_name(name: str, price: float):
    bun = Bun(name, price)

    assert bun.get_name() == name


@pytest.mark.parametrize(
    "name,price",
    [
        ("sesame bun", 45.0),
        ("plain bun", 80.5),
    ],
)
def test_bun_get_price_returns_price(name: str, price: float):
    bun = Bun(name, price)

    assert bun.get_price() == price


@pytest.mark.parametrize(
    "ingredient_type,name,price",
    [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 10.0),
        (INGREDIENT_TYPE_FILLING, "cutlet", 35.5),
    ],
)
def test_ingredient_get_type_returns_type(
    ingredient_type: str, name: str, price: float
):
    ingredient = Ingredient(ingredient_type, name, price)

    assert ingredient.get_type() == ingredient_type


@pytest.mark.parametrize(
    "ingredient_type,name,price",
    [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 10.0),
        (INGREDIENT_TYPE_FILLING, "cutlet", 35.5),
    ],
)
def test_ingredient_get_name_returns_name(
    ingredient_type: str, name: str, price: float
):
    ingredient = Ingredient(ingredient_type, name, price)

    assert ingredient.get_name() == name


@pytest.mark.parametrize(
    "ingredient_type,name,price",
    [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 10.0),
        (INGREDIENT_TYPE_FILLING, "cutlet", 35.5),
    ],
)
def test_ingredient_get_price_returns_price(
    ingredient_type: str, name: str, price: float
):
    ingredient = Ingredient(ingredient_type, name, price)

    assert ingredient.get_price() == price
