import pytest
import allure
from praktikum.bun import Bun
from helpers.create_objects import create_bun


@allure.story('Проверка класса Bun')
class TestBun:

    @allure.title('Проверка корректного создания объекта Bun')
    @allure.description('self.name и self.price соответствуют указанным')
    @pytest.mark.parametrize('bun_name, bun_price',
                             [
                                 ('test_bun', 55.5)
                             ]
                             )
    def test_creation_object_bun(self, bun_name, bun_price):
        new_bun = Bun(bun_name, bun_price)
        assert new_bun.name == bun_name and new_bun.price == bun_price

    @allure.title('Проверка метода get_name')
    @allure.description('Метод get_name() возвращает self.name')
    # Проверка метода get_name
    def test_bun_get_name_method(self):
        new_bun, new_bun_name, _ = create_bun()
        assert new_bun.get_name() == new_bun_name

    @allure.title('Проверка метода get_price')
    @allure.description('Метод get_price() возвращает self.price')
    def test_bun_get_price_method(self):
        new_bun, _, new_bun_price = create_bun()
        assert new_bun.get_price() == new_bun_price
