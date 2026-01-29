import pytest
from ..bun import Bun
from ..data import Data


class TestBun():
    @pytest.mark.parametrize(
        "name, price, expected_name",
        [
            (Data.bun_one, Data.price_one, Data.bun_one),
            (Data.bun_two, Data.price_two, Data.bun_two),
            (Data.bun_three, Data.price_three, Data.bun_three),
        ]
    )
    def test_get_name(self, name, price, expected_name):
        bun = Bun(name, price)

        assert bun.get_name() == expected_name

    @pytest.mark.parametrize(
        "name, price, expected_price",
        [
            (Data.bun_one, Data.price_one, Data.price_one),
            (Data.bun_two, Data.price_two, Data.price_two),
            (Data.bun_three, Data.price_three, Data.price_three),
        ]
    )
    def test_get_price(self, name, price, expected_price):
        bun = Bun(name, price)

        assert bun.get_price() == expected_price

    def test_price_type(self):
        bun = Bun(Data.bun_one, 100.0)
        assert isinstance(bun.get_price(), float)


    def test_name_type(self):
        bun = Bun(Data.bun_one, Data.price_one)
        assert isinstance(bun.get_name(), str)
