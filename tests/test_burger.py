import pytest
from burger import Burger
from bun import Bun
from ingredient import Ingredient


@pytest.fixture
def bun():
    return Bun("black bun", 100)


@pytest.fixture
def ingredients():
    return [
        Ingredient("SAUCE", "hot sauce", 100),
        Ingredient("SAUCE", "sour cream", 200),
        Ingredient("FILLING", "cutlet", 100)
    ]


def test_burger_creation(bun, ingredients):
    burger = Burger()
    burger.set_buns(bun)
    for ingredient in ingredients:
        burger.add_ingredient(ingredient)

    assert burger.get_price() == 600  # 100*2 + 100 + 200 + 100


def test_burger_receipt(bun, ingredients):
    burger = Burger()
    burger.set_buns(bun)
    for ingredient in ingredients:
        burger.add_ingredient(ingredient)

    receipt = burger.get_receipt()
    assert "(==== black bun ====)" in receipt
    assert "= sauce hot sauce =" in receipt
    assert "= sauce sour cream =" in receipt
    assert "= filling cutlet =" in receipt
    assert "Price: 600" in receipt


def test_move_ingredient(bun, ingredients):
    burger = Burger()
    burger.set_buns(bun)
    for ingredient in ingredients:
        burger.add_ingredient(ingredient)

    burger.move_ingredient(0, 2)
    assert burger.ingredients[2].get_name() == "hot sauce"


def test_remove_ingredient(bun, ingredients):
    burger = Burger()
    burger.set_buns(bun)
    for ingredient in ingredients:
        burger.add_ingredient(ingredient)

    burger.remove_ingredient(1)
    assert len(burger.ingredients) == 2
