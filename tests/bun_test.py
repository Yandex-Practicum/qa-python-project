from praktikum.bun import Bun
import data_for_tests as dft


class TestBun:

    # Тест 001 - Позитивный - Проверка получения названия булочки
    def test_get_name_of_bun(self):
        bun = Bun(dft.name_of_bun, dft.price_of_bun)
        result = bun.get_name()

        assert dft.name_of_bun == result, \
            f'Название булочки "{result}", а должно быть "{dft.name_of_bun}"!'

    # Тест 002 - Позитивный - Проверка получения цены булочки
    def test_get_price_of_bun(self):
        bun = Bun(dft.name_of_bun, dft.price_of_bun)
        result = bun.get_price()

        assert dft.price_of_bun == result, \
            f'Цена булочки "{result}", а должна быть "{dft.price_of_bun}"!'
