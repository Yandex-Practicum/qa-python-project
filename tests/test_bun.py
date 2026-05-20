import pytest

from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200.5)
    ])
    def test_getters_return_correct_bun_data(self, name, price):
        bun = Bun(name, price)

        assert bun.get_name() == name
        assert bun.get_price() == price