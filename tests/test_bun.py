from data import Data
from praktikum.bun import Bun


class TestBun:

    def test_create_new_bun_successful(self):
        """Проверка создания булки. ОР: Новые булки создаются с установленным названием и ценой"""
        new_bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)

        assert new_bun.get_name() == Data.BUN_NAME and new_bun.get_price() == Data.BUN_PRICE, \
            f'Название булки {new_bun.get_name()} не совпадает с названием - {Data.BUN_NAME}. ' \
            f'Цена за булку - {new_bun.get_price()} не совпадает с установленной ценой {Data.BUN_PRICE}'

    def test_bun_get_name_one_bun_successful(self):
        """Проверка назначения имени булки. ОР: Новая булка создается с установленным названием"""
        new_bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)

        assert new_bun.get_name() == Data.BUN_NAME,\
            f'Название булки {new_bun.get_name()} не совпадает с названием - {Data.BUN_NAME}. '

    def test_bun_get_price_one_bun_successful(self):
        """Проверка назначения цены булки. ОР: Новые булки создаются с установленной ценой"""
        new_bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)

        assert new_bun.get_price() == Data.BUN_PRICE,\
            f'Цена за булку - {new_bun.get_price()} не совпадает с установленной ценой {Data.BUN_PRICE}'
