import pytest
import allure

from praktikum.bun import Bun



class TestBun:

    @allure.title('Тестирование создания экземпляра Bun')
    @allure.description('Проверка, что создан экземпляр с переменными, чьи значения равны заанным при создании')
    @pytest.mark.parametrize('name,price', [
        ['Bulka',100],
        [None, None],
        ['Bulka', None],
        [None, 100]
    ])
    def test_init(self, name, price):
        bun = Bun(name, price)
        assert (bun.name == name) and (bun.price == price)


    @allure.title('Тестирование метода get_name()')
    @allure.description('Сравниваем результаты работы метода и значение name')
    def test_get_name(self, bun_creation):
        bun = bun_creation
        assert (bun.get_name()== bun.name)


    @allure.title('Тестирование метода get_price()')
    @allure.description('Сравниваем результаты работы метода и переменной price')
    def test_get_price(self, bun_creation):
        bun = bun_creation
        assert (bun.price == bun.get_price())


