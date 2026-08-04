def test_set_buns(burger_with_data):
    burger, bun, ingredient1, ingredient2 = burger_with_data
    burger.set_buns(bun)
    assert burger.bun == bun


def test_add_ingredient(burger_with_data):
    burger, bun, ingredient1, ingredient2 = burger_with_data
    burger.add_ingredient(ingredient1)
    assert burger.ingredients == [ingredient1]


def test_add_two_ingredients(burger_with_data):
    burger, bun, ingredient1, ingredient2 = burger_with_data
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    assert burger.ingredients == [ingredient1, ingredient2]


def test_remove_ingredient(burger_with_data):
    burger, bun, ingredient1, ingredient2 = burger_with_data
    burger.add_ingredient(ingredient1)
    burger.remove_ingredient(0)
    assert burger.ingredients == []


def test_move_ingredient(burger_with_data):
    burger, bun, ingredient1, ingredient2 = burger_with_data
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    assert burger.ingredients == [ingredient1, ingredient2]
    burger.move_ingredient(0, 1)
    assert burger.ingredients == [ingredient2, ingredient1]


def test_get_price(burger_with_data):
    burger, bun, ingredient1, ingredient2 = burger_with_data
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    assert burger.get_price() == 400


def test_get_receipt(burger_with_data):
    burger, bun, ingredient1, ingredient2 = burger_with_data
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    expected_receipt = (
        "(==== black bun ====)\n"
        "= sauce hot sauce =\n"
        "= filling cutlet =\n"
        "(==== black bun ====)\n"
        "\n"
        "Price: 400"
    )
    assert burger.get_receipt() == expected_receipt
def test_get_receipt(burger_with_data):
    burger, bun, ingredient1, ingredient2 = burger_with_data
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    expected_receipt = (
        "(==== black bun ====)\n"
        "= sauce hot sauce =\n"
        "= filling cutlet =\n"
        "(==== black bun ====)\n"
        "\n"
        "Price: 400"
    )
    assert burger.get_receipt() == expected_receipt

