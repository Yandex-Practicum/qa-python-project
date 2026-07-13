import pytest


class TestBun:

    def test_get_name_returns_name(self, black_bun):
        assert black_bun.get_name() == "black bun"

    def test_get_price_returns_price(self, black_bun):
        assert black_bun.get_price() == 100

    @pytest.mark.parametrize(
        "bun, expected_name, expected_price",
        [
            (("black bun", 100), "black bun", 100),
            (("white bun", 200), "white bun", 200),
            (("", 0), "", 0),
        ],
        indirect=["bun"],
    )
    def test_init_sets_attributes(self, bun, expected_name, expected_price):
        assert bun.get_name() == expected_name
        assert bun.get_price() == expected_price
