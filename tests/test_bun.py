from praktikum.bun import Bun
import allure


@allure.feature('Bun')
class TestBun:

    @allure.title('Check bun name is set correctly in constructor')
    def test_name_of_bun_return_correct(self):
        bun = Bun(name='Флюорисцентная булка R2-D3', price=3100.56)
        assert bun.name == 'Флюорисцентная булка R2-D3', f"Expected name 'Флюорисцентная булка R2-D3', but got '{bun.name}'"

    @allure.title('Check bun name data type is string')
    def test_name_of_bun_is_string(self):
        bun = Bun(name='Флюорисцентная булка R2-D3', price=3100.56)
        assert isinstance(bun.name, str), f"Expected name to be str, but got {type(bun.name)}"

    @allure.title('Check bun price is set correctly in constructor')
    def test_price_of_bun_return_correct(self):
        bun = Bun(name='Флюорисцентная булка R2-D3', price=3100.56)
        assert bun.price == 3100.56, f"Expected price 3100.56, but got {bun.price}"

    @allure.title('Check bun price data type is float')
    def test_price_of_bun_is_float(self):
        bun = Bun(name='Флюорисцентная булка R2-D3', price=3100.56)
        assert isinstance(bun.price, float), f"Expected price to be float, but got {type(bun.price)}"

    @allure.title('Check get_name() method returns correct value')
    def test_get_name_returns_correct_value(self):
        bun = Bun('Краторная булка N200-i', 4567.50)
        assert bun.get_name() == 'Краторная булка N200-i', f"Expected name 'Краторная булка N200-i', btu got {bun.get_name}"

    @allure.title('Check get_price() method returns correct value')
    def test_get_price_returns_correct_value(self):
        bun = Bun('Краторная булка N200-i', 4567.50)
        assert bun.get_price() == 4567.50, f"Expected price 4567.50, but got {bun.get_price}"
