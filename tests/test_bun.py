import pytest
import allure
from bun import Bun


@allure.feature("Bun Class Tests")
class TestBun:
    @pytest.mark.parametrize("name", ["Whole Wheat Bun", "Potato Bun", "Brioche Bun"])
    @allure.title("Test Bun Name Parameterized")
    @allure.step("Testing Bun names with different values")
    def test_bun_get_name(self, name):
        price = 50.0
        bun = Bun(name, price)

        assert bun.get_name() == name

    @pytest.mark.parametrize("price", [40.0, 30.5, 55.5])
    @allure.title("Test Bun Price Parameterized")
    @allure.step("Testing Bun prices with different values")
    def test_bun_get_price(self, price):
        name = "Test Bun"
        bun = Bun(name, price)

        assert bun.get_price() == price
