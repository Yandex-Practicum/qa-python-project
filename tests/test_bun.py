import allure
import pytest
from Stellar_Burgers.bun import Bun

@allure.feature('Проверка создания булочки с разными параметрами')
class TestBun:
    @allure.title('Проверка имени булочки с параметрами: {name}, {price}')
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
    ])
    def test_bun_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name, f"Имя булочки должно быть {name}"

    @allure.title('Проверка цены булочки с параметрами: {name}, {price}')
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
    ])
    def test_bun_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price, f"Цена булочки должна быть {price}"

