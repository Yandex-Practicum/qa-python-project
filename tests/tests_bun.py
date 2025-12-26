from unittest.mock import Mock

import pytest
from data import bun_name
from conftest import bun_object
from praktikum import bun
from praktikum.bun import Bun


class TestBun:
    def test___init__name(self):
        bun_1 = Bun('mozarella', 4.6)
        assert bun_1.get_name() == "mozarella"

    def test___init__price(self):
        bun_1 = Bun('mozarella', 4.6)
        assert bun_1.get_price() == 4.6

    def test_constructor_name(self):
        new_bun = Bun('Classic Bun', 4.6)
        assert new_bun.name == 'Classic Bun'

    def test_constructor_price(self):
        new_bun = Bun('Classic Bun', 4.6)
        assert new_bun.price == 4.6

    def test_get_name_str_name_return_name(self, bun_object):
        assert bun_object.get_name() == 'Classic Bun'

    def test_get_price_number_return_number(self, bun_object):
        assert bun_object.get_price() == 1.5

    def test_initialization_get_name_return_name(self, bun_object):
        bun_object.name = 'burger'
        assert bun_object.get_name() == 'burger'

    def test_initialization_get_price_return_name(self, bun_object):
        bun_object.price = 6
        assert bun_object.get_price() == 6

    def test_get_price_negative_price_get_price(self, bun_object):
        bun_object.price = -3
        assert bun_object.get_price() == -3

    def test_set_price(self, bun_object):
        bun_object.price = 8.0
        assert bun_object.get_price() == 8.0

    def test_create_object(self):
        bun_object = Bun('black bun', 66)
        assert bun_object.name == 'black bun'

    def test_create_object_(self):
        bun_object = Bun('black bun', 66)
        assert bun_object.price == 66

    def test_initialization(self, bun_object):
        assert bun_object.name == "Classic Bun"
        assert abs(bun_object.price - 1.5) < 0.01

    def test_set_name(self, bun_object):
        bun_object.name = "Sesame Bun"
        assert bun_object.get_name() == "Sesame Bun"


