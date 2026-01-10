import allure
from praktikum.burger import Burger
from unittest.mock import Mock

class TestBurger:

    @allure.title('Установка булки')
    def test_set_buns(self):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.name = 'Булка'
        burger.set_buns(bun_mock.name)
        assert burger.bun == 'Булка'

    @allure.title('Добавление ингредиента')
    def test_add_ingredient(self):
        burger = Burger()
        ingr_mock = Mock()
        ingr_mock.name = 'Начинка'
        burger.add_ingredient(ingr_mock.name)
        assert burger.ingredients[0] == ingr_mock.name

    @allure.title('Удаление ингредиента')
    def test_remove_ingredient(self):
        burger = Burger()
        ingr_mock = Mock()
        ingr_mock.name = 'Начинка'
        burger.add_ingredient(ingr_mock.name)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    @allure.title('Перемещение ингредиента')
    def test_move_ingredient(self):
        burger = Burger()
        ingr_mock = Mock()
        ingr_mock.first = 'Ингредиент 1'
        ingr_mock.second = 'Ингредиент 2'
        burger.add_ingredient(ingr_mock.first)
        burger.add_ingredient(ingr_mock.second)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingr_mock.second and burger.ingredients[1] == ingr_mock.first

    @allure.title('Получение цены')
    def test_get_price(self):
        burger = Burger()
        bun_mock = Mock()
        ingr_mock = Mock()
        bun_mock.get_price.return_value = 100
        ingr_mock.get_price.return_value = 20
        burger.bun = bun_mock
        burger.add_ingredient(ingr_mock)  
        result = 220
        assert result == burger.get_price()

    @allure.title('Печать чека')
    def test_print_receipt(self):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.get_name.return_value = 'Булка'
        bun_mock.get_price.return_value = 100
        ingr_mock = Mock()
        ingr_mock.get_type.return_value = 'Соус'
        ingr_mock.get_name.return_value = 'Кетчуп'
        ingr_mock.get_price.return_value = 20
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingr_mock)
        receipt = burger.get_receipt()
        assert 'Булка' in receipt and 'соус Кетчуп' in receipt and 'Price: 220' in receipt
