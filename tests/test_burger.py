import pytest
import allure
from unittest.mock import Mock 

from praktikum.burger import Burger
from helpers import CreateObject



# Здесь создание булки и ингридиентов вынесены не в фикстуры, а в функции, потому что в методах нужно создавать более одного ингридиента и комбинацию булки и ингридиентов.
# А писать одну фразу burger = Burger() в тесте  а) короче, чем название фикстуры в параметрах, потом в теле,   б) быстрее и экономнее, чем вызывать отдельную фикстуру и передавать из нее данные.


class TestBurger:


    @allure.title('Тестирование создания экземпляра burger')
    @allure.description('Проверка, что создан экземпляр класса Burger, у него есть переменная bun со значением None и пустой список ingredients')
    def test_init (self):
        burger = Burger()
        assert \
            (burger) and \
            (burger.bun is None) and \
            (burger.ingredients == [])


    @allure.title('Тестирование метода set_buns()')
    @allure.description('Сравниваем исходную булочку и то, что возвращает метод set_buns()')
    def test_set_buns (self):
        mock_bun = CreateObject.create_mock_bun()
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun==mock_bun


    @allure.title('Тестирование метода add_ingredient()')
    @allure.description('Сравниваем исходный список ингредиентов и то, что возвращает метод add_ingredient()')
    def test_add_ingredient (self):
        mock_ingredient = CreateObject.create_mock_ingredient()
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients


    @allure.title('Тестирование метода remove_ingredient()')
    @allure.description('Сравниваем исходный список ингридиентов без одного из них с результатом работы метода remove_ingredient()')
    def test_remove_ingredient (self):
        ingr1 = CreateObject.create_mock_ingredient()
        ingr2 = CreateObject.create_mock_ingredient()
        ingr3 = CreateObject.create_mock_ingredient()
        burger = Burger()
        burger.ingredients = [ingr1, ingr2, ingr3]
        burger.remove_ingredient(2)
        assert burger.ingredients == [ingr1, ingr2]



    @allure.title('Тестирование метода move_ingredient()')
    @allure.description('Сравниваем исходный список ингредиентов с поменяными местами ингредиентами с результатов работы метода move_ingredient()')
    def test_move_ingredient (self):
        ingr1 = CreateObject.create_mock_ingredient()
        ingr2 = CreateObject.create_mock_ingredient()
        ingr3 = CreateObject.create_mock_ingredient()
        burger = Burger()
        burger.ingredients = [ingr1, ingr2, ingr3]
        burger.move_ingredient(0,1)
        assert burger.ingredients == [ingr2, ingr1, ingr3]


    @allure.title('Тестирование метода get_price()')
    @allure.description('Сравниваем сумму цен всех компонентов и результат работы метода get_price()')
    def test_get_price(self):
        mock_bun = CreateObject.create_mock_bun()
        ingrs_moks = CreateObject.create_list_mock_ingredients(4)
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = ingrs_moks

        assert (burger.get_price() == (mock_bun.price*2 + CreateObject.calculate_price_list_ingredients(ingrs_moks)))


    @allure.title('Тестирование метода get_receipt()')
    @allure.description('Сравниваем: 1. Количество строк чека равно кол-во ингредиентов + 2 (булки) + 2 (пустая строка и строка с ценой).     2. Цена в чеке совпадает с расчетной')
    def test_get_receipt(self):
        num_ingr = 4
        mock_bun = CreateObject.create_mock_bun()
        ingrs_moks = CreateObject.create_list_mock_ingredients(num_ingr)
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = ingrs_moks
        burger_price_to_be = mock_bun.price*2 + CreateObject.calculate_price_list_ingredients(ingrs_moks)

        receipt_from_classBurger = burger.get_receipt()

        receipt_to_be = f'(==== {mock_bun.name} ====)\n'
        for ingr in ingrs_moks:
            receipt_to_be += f'= {ingr.type.lower()} {ingr.name} =\n'
        receipt_to_be += f'(==== {mock_bun.name} ====)\n\n'
        receipt_to_be += f'Price: {burger_price_to_be}' 

        
        assert (receipt_from_classBurger == receipt_to_be)




"""
(==== bulka_jrwx ====)
= sauce ingr_duyq =
= sauce ingr_ychh =
= sauce ingr_mivg =
(==== bulka_jrwx ====)
"""