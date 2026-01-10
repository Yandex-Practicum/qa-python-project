import pytest
from praktikum.bun import Bun

class TestBun:
    @pytest.fixture
    def bun(self):
        return Bun("white bun", 200)

    @pytest.mark.parametrize("expected_name, expected_price", [
        ("white bun", 200),
        ("black bun", 250)
    ])
    def test_bun_properties(self, expected_name, expected_price):
        bun = Bun(expected_name, expected_price)
        assert bun.get_name() == expected_name
        assert bun.get_price() == expected_price
