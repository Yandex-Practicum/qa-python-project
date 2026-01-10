import pytest

class TestBun:
    def test_bun_creation(self, kunzhutnaya_bun):
        assert kunzhutnaya_bun.name == "Кунжутная"
        assert kunzhutnaya_bun.price == 3.50

    def test_get_name(self, kunzhutnaya_bun):
        assert kunzhutnaya_bun.get_name() == 'Кунжутная'

    def test_get_price(self, kunzhutnaya_bun):
        assert kunzhutnaya_bun.get_price() == 3.50
