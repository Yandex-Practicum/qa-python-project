from unittest.mock import Mock
from praktikum.burger import Burger


def test_burger_get_price():
    bun = Mock()
    bun.get_price.return_value = 988

    ingredient1 = Mock()
    ingredient1.get_price.return_value = 90

    ingredient2 = Mock()
    ingredient2.get_price.return_value = 1337

    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)

    assert burger.get_price() == 3403  # 988*2 + 90 + 1337
