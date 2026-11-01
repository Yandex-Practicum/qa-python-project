import pytest

from praktikum.bun import Bun


@pytest.mark.parametrize("name, price", [
    pytest.param("black bun", 100, id="int_price"),
    pytest.param("Краторная булка", 1253.5, id="float_price"),
    pytest.param("", 0, id="empty_name_zero_price"),
])
def test_bun_getters(name, price):
    bun = Bun(name, price)

    assert bun.get_name() == name
    assert bun.get_price() == price

    