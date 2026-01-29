import pytest
from praktikum.bun import Bun

class TestBun:

    @pytest.mark.parametrize(
        "name, price",
        [
            ("Булочка", 100),
            ("black bun", 100),
            ("Красная булочка", 100),
            ("123456", 100)
        ]
    )
    def test_bun_str_type_name(self, name, price):
        assert Bun(name, price).get_name() == name

    @pytest.mark.parametrize(
        "name, price",
        [
            ("Булочка", 10.0),
            ("Булочка", 33.55),
            ("Булочка", 123456),
            ("Булочка", 0000)
        ]
    )
    def test_bun_float_and_int_type_price(self, name, price):
        assert Bun(name, price).get_price() == price


