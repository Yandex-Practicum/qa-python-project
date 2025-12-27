import sys
sys.path.insert(0,"C:/Users/alekberovalf/PycharmProjects/Diplom_1/")

import pytest
from praktikum.bun import Bun

class TestBun:

    def test_get_name(self):
        bun = Bun('Флюоресцентная булка', 988.0)
        name = bun.get_name()
        assert name == 'Флюоресцентная булка'


    def test_get_price(self):
        bun = Bun('Краторная булка', 1255.0)
        price = bun.get_price()
        assert price == 1255.0
