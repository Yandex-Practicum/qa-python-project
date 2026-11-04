from praktikum.burger import Burger


def test_new_burger_has_no_bun_and_no_ingredients():
    burger = Burger()
    assert burger.bun is None
    assert burger.ingredients == []