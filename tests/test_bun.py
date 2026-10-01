import pytest

from Task_1.bun import Bun


@pytest.mark.parametrize(
    "name, price",
    [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
    ],
)
def test_get_name_and_price(name, price):
    bun = Bun(name, price)

    assert bun.get_name() == name
    assert bun.get_price() == price