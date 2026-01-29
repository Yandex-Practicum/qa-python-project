import allure
from praktikum.bun import Bun


@allure.feature("Тестирование класса Bun")
class TestBun:

    @allure.title("Проверка создания объекта класса Bun")
    def test_create_object_for_bun(self):
        bun_tst = Bun('Булочка', 55)
        bun_tst_name = bun_tst.name
        bun_tst_price = bun_tst.price
        assert bun_tst_name == 'Булочка' and bun_tst_price == 55, \
          f'bun_tst_name is: {bun_tst_name}, bun_tst_price is {bun_tst_price}'

    @allure.title("Проверка метода возврата имени")
    def test_get_name_return_name(self):
        bun_tst = Bun('Булка', 5)
        bun_tst_name = bun_tst.get_name()
        assert bun_tst_name == 'Булка', f'bun_tst_name is: {bun_tst_name}'

    @allure.title("Проверка метода возврата стоиомсти")
    def test_get_price_return_price(self):
        bun_tst = Bun('Булка', 1.5)
        bun_tst_coast = bun_tst.get_price()
        assert bun_tst_coast == 1.5, f'bun_tst_coast is: {bun_tst_coast}'


