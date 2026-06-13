import pytest

from praktikum.bun import Bun


@pytest.mark.parametrize(
    "name, price",
    [
        ("black bun", 100),
        ("white bun", 200.5),
    ],
)
def test_bun_returns_name_and_price(name, price):
    bun = Bun(name, price)

    assert bun.get_name() == name
    assert bun.get_price() == price
