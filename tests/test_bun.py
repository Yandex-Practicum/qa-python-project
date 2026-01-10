from praktikum.bun import Bun
import pytest
import data


class TestBun:

    @pytest.mark.parametrize('name,price', [
            (data.NAME_BUN_COSMO, data.PRICE_BUN_LARGE),
            (data.NAME_BUN_COSMO, data.PRICE_BUN_FLOAT),
            (data.NAME_BUN_COSMO, data.PRICE_BUN_INT)
        ])
    def test_get_price_bun_three_bun_price_geted(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price

    @pytest.mark.parametrize('name,price', [
            (data.NAME_BUN_NO_NAME, data.PRICE_BUN_INT),
            (data.NAME_BUN_BLACK_BUN, data.PRICE_BUN_INT),
            (data.NAME_BUN_COSMO, data.PRICE_BUN_INT)
        ])
    def test_get_name_bun_three_bun_name_geted(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name