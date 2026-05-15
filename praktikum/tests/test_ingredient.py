def test_ingredient_get_name(ingredient):
    assert ingredient.get_name() == "hot sauce"


def test_ingredient_get_price(ingredient):
    assert ingredient.get_price() == 100


def test_ingredient_get_type(ingredient):
    assert ingredient.get_type() == "SAUCE"