import pytest
from praktikum.bun import Bun


class TestBun:
    @pytest.fixture
    def bun(self):
        return Bun("Cheese Bun", 2.50)

    def test_bun_constructor(self, bun):
        assert bun.name == "Cheese Bun"
        assert bun.price == 2.50

    def test_get_correct_name_successfully_get(self, bun):
        assert bun.get_name() == "Cheese Bun"

    def test_get_correct_price_successfully_get(self, bun):
        assert bun.get_price() == 2.50
