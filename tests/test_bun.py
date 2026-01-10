import pytest
from praktikum.bun import Bun


class TestingBun:

    def test_get_name(self):
        bun = Bun('Супербулка', 200)
        assert bun.get_name() == 'Супербулка'

    def test_get_price(self):
        bun = Bun('Супербулка', 200.752)
        assert bun.get_price() == 200.752
