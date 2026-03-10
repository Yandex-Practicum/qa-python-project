import pytest
from praktikum.bun import Bun
from praktikum.data import BUNS_DATA
from tests.conftest import BLACK_BUN, WHITE_BUN

class TestBun:
    @pytest.mark.parametrize("bun_data", BUNS_DATA)
    def test_bun_creation_get_name_returns_correct_name(self, bun_data):
        bun = Bun(bun_data["name"], bun_data["price"])
        assert bun.get_name() == bun_data["name"]

    @pytest.mark.parametrize("bun_data", BUNS_DATA)
    def test_bun_creation_get_price_returns_correct_price(self, bun_data):
        bun = Bun(bun_data["name"], bun_data["price"])
        assert bun.get_price() == bun_data["price"]

    def test_bun_different_objects_different_memory_addresses(self):
        assert id(BLACK_BUN) != id(WHITE_BUN)

    def test_bun_get_name_returns_string_type(self):
        result = BLACK_BUN.get_name()
        assert isinstance(result, str)
