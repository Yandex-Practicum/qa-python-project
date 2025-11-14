import allure
from praktikum.bun import Bun



class TestBun:

    @allure.title('Проверка возврата Названия')
    def test_bun_name(self):

        bun = Bun(name='Bun1', price=5.0)
        result = bun.get_name()

        assert result == 'Bun1'


    @allure.title('Проверка возврата Стоимости')
    def test_bun_price(self):

        bun = Bun(name='Bun1', price=5.0)
        result = bun.get_price()

        assert result == 5.0
