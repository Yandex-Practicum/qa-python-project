import pytest
from praktikum.bun import Bun
import data
import logging
logging.basicConfig(level=logging.INFO)


class TestBun:

    @pytest.mark.parametrize('bun_maket, expected_name, expected_price', [
        (Bun(data.BUN_NAME, data.BUN_PRICE), data.BUN_NAME, data.BUN_PRICE),
        (Bun(None, data.BUN_PRICE), None, data.BUN_PRICE),
        (Bun(data.BUN_NAME, None), data.BUN_NAME, None),
        (Bun(None, None), None, None)
    ])
    def test_bun_constructor_true(self, bun_maket, expected_name, expected_price):
        bun = bun_maket
        assert bun.name == expected_name and bun.price == expected_price, \
            (f"Ожидалось имя: {expected_name}, но получено: {bun.name}" and
             f"Ожидалась цена: {expected_price}, но получено: {bun.price}")
        logging.info(f"\nТестируемая булочка: имя = {bun.name}, цена = {bun.price}")

    def test_get_name_bun_true(self, create_bun):
        assert create_bun.get_name() == create_bun.name
        logging.info(f'\nИмя булочки: {create_bun.name}')

    def test_get_price_bun_true(self, create_bun):
        assert create_bun.get_price() == create_bun.price
        logging.info(f'\nЦена булочки: {create_bun.price}')
