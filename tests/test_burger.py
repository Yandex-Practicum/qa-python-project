from unittest.mock import Mock
from burger import Burger


def test_add_ingredient_increases_ingredients_count():
    burger = Burger()
    ingredient = Mock()

    burger.add_ingredient(ingredient)

    assert len(burger.ingredients) == 1


def test_remove_ingredient_decreases_ingredients_count():
    burger = Burger()
    ingredient = Mock()
    burger.add_ingredient(ingredient)

    burger.remove_ingredient(0)

    assert len(burger.ingredients) == 0


def test_set_buns_sets_top_and_bottom():
    burger = Burger()
    bun = Mock()
    bun.price = 100

    burger.set_buns(bun)

    assert burger.bun == bun
