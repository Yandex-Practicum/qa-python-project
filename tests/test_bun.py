import pytest
from praktikum.bun import Bun
from unittest.mock import Mock


class TestBun:
    def test_get_name_of_bun(self, create_new_bun):
        assert create_new_bun.get_name() == "black bun"

    def test_get_price_of_bun(self, create_new_bun):
        assert create_new_bun.get_price() == 100