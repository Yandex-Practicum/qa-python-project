from unittest.mock import patch, Mock
import pytest
from Diplom_1.practicum.bun import Bun
from Diplom_1.practicum.database import Database
class TestBun:

    @pytest.mark.parametrize("index", [0, 1, 2])
    def test_get_name(self, index):
        database = Database()
        bun_name = database.buns[index].get_name()
        bun_price = database.buns[index].get_price()

        bun = Bun(bun_name, bun_price)
        assert bun.get_name() == bun_name


    @pytest.mark.parametrize("index", [0, 1, 2])
    def test_get_price(self, index):
        database = Database()
        bun_name = database.buns[index].get_name()
        bun_price = database.buns[index].get_price()

        bun = Bun(bun_name, bun_price)
        assert bun.get_price() == bun_price