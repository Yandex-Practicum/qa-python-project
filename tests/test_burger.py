from praktikum.bun import Bun
from praktikum.burger import Burger


def test_burger_initializes_without_bun_and_ingredients():
    burger = Burger()

    assert burger.bun is None
    assert burger.ingredients == []


def test_set_buns_sets_bun():
    burger = Burger()
    bun = Bun("black bun", 100)

    burger.set_buns(bun)

    assert burger.bun is bun
