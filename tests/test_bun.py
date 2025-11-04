import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize('name, price', [('black bun', 100), ('white bun', 200), ('red bun', 300)])
    def test_bun_creation_valid_params_returns_correct_name_and_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price