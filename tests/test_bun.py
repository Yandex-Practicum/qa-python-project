import pytest
from practikum.bun import Bun
from conftest import TEST_BUNS


@pytest.mark.parametrize("bun_data", TEST_BUNS)
def test_bun_creation(bun_data):
    bun = Bun(bun_data["name"], bun_data["price"])
    assert bun.get_name() == bun_data["name"]
    assert bun.get_price() == bun_data["price"]
