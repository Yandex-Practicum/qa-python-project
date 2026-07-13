from unittest.mock import Mock

def test_set_bun(burger):
    bun = Mock()
    burger.set_buns(bun)
    assert burger.bun == bun

def test_add_ingredient(burger, sauce):
    burger.add_ingredient(sauce)
    assert sauce in burger.ingredients

def test_remove_ingredient(burger, sauce, filling):
    burger.add_ingredient(sauce)
    burger.add_ingredient(filling)
    burger.remove_ingredient(0)
    assert burger.ingredients == [filling]

def test_move_ingredient(burger, sauce, filling):
    burger.add_ingredient(sauce)
    burger.add_ingredient(filling)
    burger.move_ingredient(0, 1)
    assert burger.ingredients == [filling, sauce]

def test_get_price(burger):
    bun = Mock()
    bun.get_price.return_value = 200
    ingredient1 = Mock()
    ingredient1.get_price.return_value = 100

    ingredient2 = Mock()
    ingredient2.get_price.return_value = 300
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    assert burger.get_price() == 800

def test_get_receipt(burger):
    bun = Mock()
    bun.get_name.return_value = "white bun"
    bun.get_price.return_value = 200

    ingredient = Mock()
    ingredient.get_type.return_value = "SAUCE"
    ingredient.get_name.return_value = "hot sauce"
    ingredient.get_price.return_value = 100
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    expected = (
        "(==== white bun ====)\n"
        "= sauce hot sauce =\n"
        "(==== white bun ====)\n\n"
        "Price: 500"
    )
    assert burger.get_receipt() == expected
