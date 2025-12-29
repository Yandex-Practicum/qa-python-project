from unittest.mock import Mock
from burger import Burger


def test_set_buns():
    burger = Burger()
    bun = Mock()
    bun.get_price.return_value = 100

    burger.set_buns(bun)

    assert burger.bun == bun


def test_add_ingredient():
    burger = Burger()
    ingredient = Mock()

    burger.add_ingredient(ingredient)

    assert ingredient in burger.ingredients


def test_remove_ingredient():
    burger = Burger()
    ingredient = Mock()
    burger.ingredients = [ingredient]

    burger.remove_ingredient(0)

    assert ingredient not in burger.ingredients


def test_move_ingredient():
    burger = Burger()
    ingredient_1 = Mock()
    ingredient_2 = Mock()
    burger.ingredients = [ingredient_1, ingredient_2]

    burger.move_ingredient(0, 1)

    assert burger.ingredients == [ingredient_2, ingredient_1]



def test_get_price():
    burger = Burger()

    bun = Mock()
    bun.get_price.return_value = 100

    ingredient_1 = Mock()
    ingredient_1.get_price.return_value = 50

    ingredient_2 = Mock()
    ingredient_2.get_price.return_value = 70

    burger.set_buns(bun)
    burger.add_ingredient(ingredient_1)
    burger.add_ingredient(ingredient_2)

    assert burger.get_price() == 320


def test_get_receipt():
    burger = Burger()

    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100

    ingredient = Mock()
    ingredient.get_type.return_value = "SAUCE"
    ingredient.get_name.return_value = "hot sauce"
    ingredient.get_price.return_value = 50

    burger.set_buns(bun)
    burger.add_ingredient(ingredient)

    receipt = burger.get_receipt()

    assert "black bun" in receipt
    assert "hot sauce" in receipt
    assert "Price: 250" in receipt