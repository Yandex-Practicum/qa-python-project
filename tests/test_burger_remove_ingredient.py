

def test_burger_remove_ingredient_burger_has_no_ingredient(burger, ingredient_mock):
    burger.add_ingredient(ingredient_mock)
    burger.remove_ingredient(0)
    assert burger.ingredients == []
