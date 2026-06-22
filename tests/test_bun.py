import pytest
import allure
from praktikum.bun import Bun

@allure.epic("Stellar Burgers")
@allure.feature("Юнит-тесты компонентов: Булочка")
class TestBun:
    @allure.title("Проверка получения названия булочки")
    @pytest.mark.parametrize("bun_name", ["Флюоресцентная булка R2-D3",
                                          "Краторная булка N-200i",
                                          ""])
    def test_get_name_filled_string_returns_same_string(self, bun_name):
        with allure.step(f"Инициализировать булочку с названием: '{bun_name}' и ценой 100.0"):
            bun = Bun(bun_name, 100.0)
        with allure.step("Вызвать метод get_name() и проверить возвращаемое значение"):
            assert bun.get_name() == bun_name

    @allure.title("Проверка получения цены булочки")
    @pytest.mark.parametrize("bun_price", [
        100.0, 
        0.0, 
        999.99
    ])
    def test_get_price_various_amounts_returns_same_amount(self, bun_price):
        with allure.step(f"Инициализировать булочку с названием 'Стандартная' и ценой: {bun_price}"):
            bun = Bun("Стандартная", bun_price)
        with allure.step("Вызвать метод get_price() и проверить возвращаемое значение"):
            assert bun.get_price() == bun_price