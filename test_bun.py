import pytest
from bun import Bun

class TestBun:

    # Тестируем только разные имена (цена всегда 100)
    @pytest.mark.parametrize(
        "name",
        [
            "Краторная булка",
            "Флюоресцентная булка",
            "",
            "A",
            "Очень-очень длинное название для булочки бургера"
        ]
    )
    def test_bun_get_name(self, name):
        bun = Bun(name, 100)
        assert bun.get_name() == name

    # Тестируем только разные цены (имя всегда "Стандартная булка")
    @pytest.mark.parametrize(
        "price",
        [
            100,
            999.99,
            0,
            -100
        ]
    )
    def test_bun_get_price(self, price):
        bun = Bun("Стандартная булка", price)
        assert bun.get_price() == price
