
def test_burger_add_ingredient_burger_has_ingredient(burger, ingredient_mock):
    burger.add_ingredient(ingredient_mock)
    assert burger.ingredients[0] == ingredient_mock
    