import pytest
from bun import Bun

class TestBun:

    @pytest.mark.parametrize(
        "name, price",
        [
            ("Краторная булка", 100),
            ("Флюоресцентная булка", 999.99),
            ("", 0),
            ("A", -50),
            ("Очень-очень длинное название для булочки бургера", 1000)
        ]
    )
    def test_bun_init_and_getters(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price
