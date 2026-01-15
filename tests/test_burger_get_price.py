import pytest


@pytest.mark.parametrize("bun_price,ingredient_price,expected", [
    (100, 50, 250),
    (200, 0, 400)
])
def test_burger_get_price_returns_right_sum(burger, bun_mock, ingredient_mock,
                                            bun_price, ingredient_price, expected):
    bun_mock.get_price.return_value = bun_price
    ingredient_mock.get_price.return_value = ingredient_price
    burger.set_buns(bun_mock)
    burger.add_ingredient(ingredient_mock)
    assert burger.get_price() == expected
