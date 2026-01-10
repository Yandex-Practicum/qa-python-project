import pytest
from Diplom_1.burger import Bun  # Импортируйте ваш класс Bun из нужного модуля

class TestBun:
    @pytest.fixture
    def setup(self):
        bun = Bun(name="Test Bun", price=1.5)
        return bun

    def test_get_name(self, setup):
        bun = setup
        assert bun.get_name() == "Test Bun"

    def test_get_price(self, setup):
        bun = setup
        assert bun.get_price() == 1.5

    def test_bun_initialization(self, setup):
        bun = setup
        assert bun.name == "Test Bun"
        assert bun.price == 1.5