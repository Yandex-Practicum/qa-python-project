import pytest

from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize("name", ["Бриошь", "Рисовая", " ", ""])
    def test_return_correct_name_when_bun_is_created(self, name):
        bun = Bun(name, 1.5)

        assert bun.get_name() == name
        assert bun.name == name

    @pytest.mark.parametrize("price", [5, -5, 0.0, 1.5])
    def test_return_correct_price_when_bun_is_created(self, price):
        bun = Bun("fake_bun", price)

        assert bun.get_price() == price
        assert bun.price == price
