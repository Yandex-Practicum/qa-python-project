import pytest
from praktikum.bun import Bun
from data import Data


class TestBun:
    """
    Тестирование класса Bun (булочка для бургера).
    Проверяет корректность работы методов get_name() и get_price().
    """

    @pytest.mark.parametrize(
        'bun_name, bun_price',
        [
            (Data.BLACK_BUN, Data.BLACK_BUN_PRICE),
            (Data.RED_BUN, Data.RED_BUN_PRICE),
            (Data.WHITE_BUN, Data.WHITE_BUN_PRICE)
        ]
    )
    def test_get_name_should_return_correct_bun_name(self, bun_name, bun_price):
        """Проверяет, что get_name() возвращает корректное название булочки."""
        bun = Bun(bun_name, bun_price)
        assert bun.get_name() == bun_name

    @pytest.mark.parametrize(
        'bun_name, bun_price',
        [
            (Data.BLACK_BUN, Data.BLACK_BUN_PRICE),
            (Data.RED_BUN, Data.RED_BUN_PRICE),
            (Data.WHITE_BUN, Data.WHITE_BUN_PRICE)
        ]
    )
    def test_get_price_should_return_correct_bun_price(self, bun_name, bun_price):
        """Проверяет, что get_price() возвращает корректную цену булочки."""
        bun = Bun(bun_name, bun_price)
        assert bun.get_price() == bun_price