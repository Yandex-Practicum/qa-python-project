import pytest

import data
from praktikum.bun import Bun


class TestBun():

    def test_get_mame__positive_value(self, mock_bun):
        testbun = Bun(mock_bun.name, mock_bun.price)
        assert testbun.get_name() == data.DEF_BUN_NAME, "Не корректный метод get_name"

    def test_get_price_positive_value(self, mock_bun):
        testbun = Bun(mock_bun.name, mock_bun.price)
        assert testbun.get_price() == data.DEF_BUN_PRICE, "Не корректный метод get_price"
