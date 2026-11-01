"""Данные для параметризации — отдельно от логики тестов."""
import pytest

PRICE_CASES = [
    pytest.param(50.0, [30.0, 20.0], 150.0, id="two_ingredients"),
    pytest.param(100.0, [50.0], 250.0, id="one_ingredient"),
    pytest.param(1253.0, [15.0], 2521.0, id="crater_bun_with_sauce"),
    pytest.param(10.0, [], 20.0, id="only_buns"),
    pytest.param(10.5, [0.1, 0.2], 21.3, id="float_prices"),
    pytest.param(0.0, [0.0], 0.0, id="zero_prices"),
]

# (src, dst) для трёх ингредиентов a, b, c
MOVE_CASES = [
    pytest.param(1, 0, id="middle_to_first"),
    pytest.param(0, 2, id="first_to_last"),
    pytest.param(2, 0, id="last_to_first"),
    pytest.param(1, 1, id="same_position"),
]

# (bun_name, bun_price, [(type, name, price), ...], expected_receipt)
RECEIPT_CASES = [
    pytest.param(
        "Краторная булка", 1253.0,
        [("SAUCE", "кисло-сладкий", 15.0)],
        "(==== Краторная булка ====)\n"
        "= sauce кисло-сладкий =\n"
        "(==== Краторная булка ====)\n"
        "\n"
        "Price: 2521.0",
        id="one_sauce",
    ),
    pytest.param(
        "Флюоресцентная булка", 988.0,
        [("FILLING", "мясо бессмертных моллюсков", 1337.0)],
        "(==== Флюоресцентная булка ====)\n"
        "= filling мясо бессмертных моллюсков =\n"
        "(==== Флюоресцентная булка ====)\n"
        "\n"
        "Price: 3313.0",
        id="one_filling",
    ),
    pytest.param(
        "Булка", 100.0,
        [("SAUCE", "соус", 10.0), ("FILLING", "котлета", 50.0)],
        "(==== Булка ====)\n"
        "= sauce соус =\n"
        "= filling котлета =\n"
        "(==== Булка ====)\n"
        "\n"
        "Price: 260.0",
        id="order_of_two_ingredients",
    ),
    pytest.param(
        "Булка", 10.0, [],
        "(==== Булка ====)\n"
        "(==== Булка ====)\n"
        "\n"
        "Price: 20.0",
        id="no_ingredients",
    ),
]

