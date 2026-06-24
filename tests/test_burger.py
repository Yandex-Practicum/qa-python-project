from unittest.mock import Mock

from praktikum.burger import Burger


def test_set_buns_sets_bun():
    burger = Burger()

    bun = Mock()
    burger.set_buns(bun)

    assert burger.bun == bun


def test_add_ingredient_adds_ingredient():
    burger = Burger()

    ingredient = Mock()
    burger.add_ingredient(ingredient)

    assert ingredient in burger.ingredients


def test_remove_ingredient_removes_ingredient():
    burger = Burger()

    ingredient_1 = Mock()
    ingredient_2 = Mock()

    burger.add_ingredient(ingredient_1)
    burger.add_ingredient(ingredient_2)

    burger.remove_ingredient(0)

    assert burger.ingredients == [ingredient_2]


def test_move_ingredient_changes_order():
    burger = Burger()

    ingredient_1 = Mock()
    ingredient_2 = Mock()
    ingredient_3 = Mock()

    burger.add_ingredient(ingredient_1)
    burger.add_ingredient(ingredient_2)
    burger.add_ingredient(ingredient_3)

    burger.move_ingredient(0, 2)

    assert burger.ingredients == [
        ingredient_2,
        ingredient_3,
        ingredient_1
    ]


def test_get_price_returns_correct_price():
    burger = Burger()

    bun = Mock()
    bun.get_price.return_value = 100

    ingredient = Mock()
    ingredient.get_price.return_value = 50

    burger.set_buns(bun)
    burger.add_ingredient(ingredient)

    assert burger.get_price() == 250


def test_get_receipt_returns_correct_receipt():
    burger = Burger()

    bun = Mock()
    bun.get_name.return_value = 'black bun'

    ingredient = Mock()
    ingredient.get_type.return_value = 'SAUCE'
    ingredient.get_name.return_value = 'hot sauce'

    burger.set_buns(bun)
    burger.add_ingredient(ingredient)

    expected = (
        '(==== black bun ====)\n'
        '= sauce hot sauce =\n'
        '(==== black bun ====)\n\n'
        'Price: 0'
    )

    burger.get_price = Mock(return_value=0)

    assert burger.get_receipt() == expected