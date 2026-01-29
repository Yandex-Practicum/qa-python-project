import pytest

from bun import Bun


class TestBun:

    def test_init(self):
        bun = Bun("Булочка", 5.0)
        assert bun.get_name() == "Булочка"
        assert round(bun.get_price(), 1) == 5.0

    def test_get_name(self):
        bun = Bun("Багет", 10.0)
        name = bun.get_name()
        assert name == "Багет"

    def test_get_price(self):
        bun = Bun("Круассан", 3.5)
        price = bun.get_price()
        assert price == 3.5

    def test_get_name_not_str(self):
        bun = Bun(12513, 4.2)
        name = bun.get_name()
        assert type(name) != str

    def test_get_price_is_str(self):
        bun = Bun("Пита", "2.3")
        price = bun.get_price()
        assert type(price) != float

    def test_get_price_is_int(self):
        bun = Bun("Лаваш", 5)
        price = bun.get_price()
        assert type(price) != float

    def test_get_price_is_float(self):
        bun = Bun("Чиабата", 5.0)
        price = bun.get_price()
        assert type(price) is float
