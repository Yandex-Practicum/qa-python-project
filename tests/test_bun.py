import pytest
from practikum.bun import Bun
from practikum.constants import H_BUNS


class TestBun:

    # Тестирование получения названия булочки
    @pytest.mark.parametrize("name,price", H_BUNS)
    def test_get_name(self, name , price):
        bun = Bun(name, price)
        assert bun.get_name() == name, "Метод get_name() возвращает неверное имя."

    # Тестирование получения цены булочки
    @pytest.mark.parametrize("name,price", H_BUNS)
    def test_get_price(self, name , price):
        bun = Bun(name, price)
        assert bun.get_price() == price, "Метод get_price() возвращает неверную цену."
