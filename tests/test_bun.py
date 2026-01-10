import pytest
from diplom_1.praktikum.bun import Bun


class TestBun:
    @pytest.fixture
    def sample_bun(self):
        return Bun("Черная булочка", 150)

    # Позитивные тесты
    def test_get_name_returns_correct_name(self, sample_bun):
        assert sample_bun.get_name() == "Черная булочка"

    def test_get_price_returns_correct_price(self, sample_bun):
        assert sample_bun.get_price() == 150

    # Негативные тесты
    def test_init_with_empty_name(self):
        bun = Bun("", 150)
        assert bun.get_name() == ""

    def test_init_with_zero_price(self):
        bun = Bun("Черная булочка", 0)
        assert bun.get_price() == 0

    def test_init_with_negative_price(self):
        bun = Bun("Черная булочка", -10)
        assert bun.get_price() == -10