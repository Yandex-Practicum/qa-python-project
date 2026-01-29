import allure
import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from unittest.mock import Mock
from unittest.mock import patch
from data import PRICE_VALUE_LST_FOR_PARAMETRIZE, GET_RECEPT_EXPECTED_VALUE


@allure.feature("Тестирование класса Burger")
class TestBurger:


    @allure.title("Проверка создания объектра класса Burger")
    def test_create_object_burger(self):
        burger_tst = Burger()
        burger_tst_bun = burger_tst.bun
        burger_tst_ingridients = burger_tst.ingredients
        assert burger_tst_bun == None and burger_tst_ingridients == [], \
        f'burger_tst_bun is {burger_tst_bun}, burger_tst_ingridients is {burger_tst_ingridients}'


    @allure.title("Проверка метода set_buns")
    def test_set_buns(self):
        burger_tst = Burger()
        mock_bun = Mock(Bun)
        burger_tst.set_buns(mock_bun)
        burger_tst_bun = burger_tst.bun
        assert burger_tst_bun == mock_bun, f'burger_tst_bun is {burger_tst_bun}'


    @allure.title("Проверка метода add_ingredient")
    def test_set_ingridients(self):
        burger_tst = Burger()
        burger_tst.add_ingredient('Котлета')
        burger_tst_ingredients = burger_tst.ingredients
        assert burger_tst_ingredients == ['Котлета'], f'burger_tst_bun is {burger_tst_ingredients}'


    @allure.title("Проверка метода remove_ingredient")
    def test_remove_ingredient_add_and_remove_one_ingridient(self):
        burger_tst = Burger()
        burger_tst.add_ingredient('Котлета')
        burger_tst.remove_ingredient(0)
        burger_tst_ingridients = burger_tst.ingredients
        assert burger_tst_ingridients == [], f'burger_tst_ingridients is {burger_tst_ingridients}'


    @allure.title("Проверка метода move_ingredient")
    def test_add_ingridients_and_move_one_ingredient(self):
        burger_tst = Burger()
        burger_tst.add_ingredient('Котлета')
        burger_tst.add_ingredient('Сыр')
        burger_tst.add_ingredient('Соус')
        burger_tst.move_ingredient(0, 1)
        burger_tst_ingridiens = burger_tst.ingredients
        ingridients_for_assert = ['Сыр', 'Котлета', 'Соус']
        assert burger_tst_ingridiens == ingridients_for_assert, \
            f'burger_tst_ingridiens are {burger_tst_ingridiens}'


# тест с простыми моками и параметризацией
    @allure.title("Проверка метода get_price")
    @pytest.mark.parametrize('price_value', PRICE_VALUE_LST_FOR_PARAMETRIZE)
    def test_get_price(self, price_value):
        bun_mock = Mock()
        bun_mock.get_price.return_value = price_value['bun']
        ingridient_mock = Mock()
        ingridient_mock.get_price.return_value = price_value['ingridient']
        ingridients_mock = Mock()
        ingridients_mock = [ingridient_mock]
        burger_tst = Burger()
        burger_tst.bun = bun_mock
        burger_tst.ingredients = ingridients_mock
        burger_tst_price = burger_tst.get_price()
        total_price = 2 * bun_mock.get_price() + ingridient_mock.get_price()
        assert burger_tst_price == total_price, f'burger_tst_price is {burger_tst_price}, total_price is {total_price}'


    @allure.title("Проверка метода get_receipt")
    @patch('praktikum.burger.Burger.get_price')
    def test_get_receipt(self, burger_price):
        burger_tst = Burger()
        mock_bun = Mock()
        mock_ingridient = Mock()
        # фальшивые наполнительи для бургера созданы, лепим бургер
        burger_tst.bun = mock_bun
        burger_tst.ingredients = [mock_ingridient]
        # тяп-ляп и готов, лепим фальшивые возвращаемые значения.
        mock_bun.get_name.return_value = 'Фальшивая булочка'
        mock_ingridient.get_type.return_value = 'Название фальшивой начинки'
        mock_ingridient.get_name.return_value = 'Какая-то фальшивая начинка'
        burger_tst.get_price.return_value = 100
        # наполняем переменную результатами прогона метода
        test_str_value = burger_tst.get_receipt()
        # создаём переменную с эталонным значением
        assert test_str_value == GET_RECEPT_EXPECTED_VALUE, \
        f'test_str_value is: {test_str_value}'
