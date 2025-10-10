import allure
from praktikum.bun import Bun

@allure.feature('Bun model')
class TestBun:

    @allure.title('Getting a name of the Bun')
    def test_get_name_success(self):
        bun = Bun("Test Bun", 123)
        assert bun.get_name() == "Test Bun"
    
    @allure.title('Getting the price of the Bun')
    def test_get_price_success(self):
        bun = Bun("Test Bun", 123)
        assert bun.get_price() == 123
