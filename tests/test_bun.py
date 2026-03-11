from praktikum.bun import Bun

from tests.data.test_data import (
    BLACK_BUN_NAME,
    BLACK_BUN_PRICE,
    WHITE_BUN_NAME,
    WHITE_BUN_PRICE,
    RED_BUN_NAME,
    RED_BUN_PRICE
)



class TestBun:

    def test_bun_init(self):
        bun = Bun(BLACK_BUN_NAME, BLACK_BUN_PRICE)

        assert bun.name == BLACK_BUN_NAME
        assert bun.price == BLACK_BUN_PRICE

    def test_get_name(self):
        bun = Bun(WHITE_BUN_NAME, WHITE_BUN_PRICE)
        assert bun.get_name() == WHITE_BUN_NAME

    def test_get_price(self):
        bun = Bun(RED_BUN_NAME, RED_BUN_PRICE)
        assert bun.get_price() == RED_BUN_PRICE
