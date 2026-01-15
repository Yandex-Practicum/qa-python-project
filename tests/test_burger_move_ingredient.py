def test_burger_move_ingredient_order_changes(burger, ingredient_mock):
    burger.add_ingredient(ingredient_mock)
    burger.add_ingredient(ingredient_mock)
    burger.move_ingredient(0, 1)
    assert len(burger.ingredients) == 2
    