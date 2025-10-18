import pytest
from unittest.mock import MagicMock
from praktikum.burger import Burger

@pytest.mark.parametrize(
    "bun_price, ingredient_prices, expected",
    [
        (0, [], 0),
        (50, [], 100),             # только булка (x2)
        (80, [20], 180),           # 2*80 + 20
        (100, [10, 20, 30], 260),  # 2*100 + 60
    ],
)
def test_total_price_parametrized(bun_price, ingredient_prices, expected):
    burger = Burger()
    # мок булки
    bun = MagicMock()
    bun.get_price.return_value = bun_price
    bun.get_name.return_value = "Any Bun"
    burger.set_buns(bun)

    # моки ингредиентов
    for p in ingredient_prices:
        ing = MagicMock()
        ing.get_price.return_value = p
        ing.get_name.return_value = f"i{p}"
        # тип не важен для цены
        ing.get_type.return_value = "FILLING"
        burger.add_ingredient(ing)

    assert burger.get_price() == expected
