import pytest
from praktikum.burger import Burger
from data import *  # Используем импорт данных из фикстуры
from unittest.mock import Mock

class TestBurger:  # Класс тестов для Burger

    # Тестирование метода добавления булки
    @pytest.mark.parametrize('buns_id', [0, 1])
    def test_set_buns_true(self, buns_id, buns_with_ingred):
        burger = Burger()
        mock_bun = buns_with_ingred[0][buns_id]  # [булки], [id булки]
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun  # Проверяем, что булка добавлена корректно

    # Тестирование метода добавления ингредиента
    @pytest.mark.parametrize('ingred_id', [0, 1])
    def test_add_ingredient_true(self, ingred_id, buns_with_ingred):
        burger = Burger()
        mock_ingred = buns_with_ingred[1][ingred_id]  # [ингредиенты], [id ингредиента]
        burger.add_ingredient(mock_ingred)
        # Проверяем, что ингредиент добавился в список
        assert burger.ingredients[0] == mock_ingred

    # Тестирование метода удаления ингредиента
    def test_remove_ingredient_true(self, buns_with_ingred):
        burger = Burger()
        burger.add_ingredient(buns_with_ingred[1][0])  # Добавляем первый ингредиент
        burger.remove_ingredient(0)  # Удаляем первый ингредиент по индексу
        # Проверяем, что список ингредиентов пуст
        assert burger.ingredients == []

    # Тестирование метода перемещения ингредиента
    def test_move_ingredient_true(self, buns_with_ingred):
        burger = Burger()
        burger.add_ingredient(buns_with_ingred[1][0])  # Добавляем первый ингредиент
        burger.add_ingredient(buns_with_ingred[1][1])  # Добавляем второй
        burger.move_ingredient(1, 0)  # Перемещаем второй ингредиент на место первого
        # Проверяем, что второй ингредиент теперь на первом месте
        assert burger.ingredients[0] == buns_with_ingred[1][1]

    # Тестирование метода получения цены
    @pytest.mark.parametrize('id', [0, 1])
    def test_get_price_true(self, id, buns_with_ingred):
        burger = Burger()
        burger.set_buns(buns_with_ingred[0][id])  # Устанавливаем булку по id
        burger.add_ingredient(buns_with_ingred[1][id])  # Добавляем ингредиент по id
        # Проверка, что цена равна сумме цен булки (умноженной на 2) и ингредиента
        assert burger.get_price() == (buns_with_ingred[0][id].get_price() * 2 + buns_with_ingred[1][id].get_price())

    # Тестирование метода получения чека
    @pytest.mark.parametrize('id', [0, 1])
    def test_get_receipt(self, id, buns_with_ingred):
        burger = Burger()
        burger.set_buns(buns_with_ingred[0][id])  # Устанавливаем булку
        burger.add_ingredient(buns_with_ingred[1][id])  # Добавляем ингредиент
        # Проверка, что чек совпадает с ожидаемым, вызовом метода get_my_receipt
        assert burger.get_receipt() == BunsWithIngred.get_my_receipt(buns_with_ingred[0][id], buns_with_ingred[1][id])

    # Дополнительные тесты для полного покрытия методов

    # Тест с бургером, который содержит только булку
    def test_burger_with_only_buns(self, buns_with_ingred):
        burger = Burger()
        burger.set_buns(buns_with_ingred[0][0])  # Только булка
        expected_price = buns_with_ingred[0][0].get_price() * 2
        # Проверка цены без ингредиентов
        assert burger.get_price() == expected_price
        # Проверка чека
        expected_receipt = BunsWithIngred.get_my_receipt(
            buns_with_ingred[0][0],
            []
        )
        assert burger.get_receipt() == expected_receipt

    # Тест с бургером, но без ингредиентов
    def test_burger_without_ingredients(self, buns_with_ingred):
        burger = Burger()
        burger.set_buns(buns_with_ingred[0][0])  # Установка булки
        # Без ингредиентов
        assert burger.get_price() == buns_with_ingred[0][0].get_price() * 2
        # Чек без ингредиентов
        expected_receipt = BunsWithIngred.get_my_receipt(
            buns_with_ingred[0][0],
            []
        )
        assert burger.get_receipt() == expected_receipt
        
    # Проверка поведения при попытке удалить ингредиент с неверным индексом
    def test_remove_ingredient_invalid_index(self, buns_with_ingred):
        burger = Burger()
        burger.add_ingredient(buns_with_ingred[1][0])
        initial_ingredients = burger.ingredients.copy()
    
        # Пытаемся удалить несуществующий индекс
        try:
            burger.remove_ingredient(5)
        except IndexError:
            pass
    
        # Проверяем, что список ингредиентов остался прежним
        assert burger.ingredients == initial_ingredients


    # Проверка поведения при попытке переместить ингредиент с неверным индексом
    def test_move_ingredient_invalid_indices(self, buns_with_ingred):
        burger = Burger()
        burger.add_ingredient(buns_with_ingred[1][0])
        initial_ingredients = burger.ingredients.copy()
    
        # Пытаемся переместить с неверным индексом
        try:
            burger.move_ingredient(0, 10)
        except IndexError:
            pass
    
        # Проверяем, что список ингредиентов остался прежним
        assert burger.ingredients == initial_ingredients

    # Проверка цены, если булка не установлена
    def test_get_price_without_bun(self, buns_with_ingred):
        burger = Burger()
        burger.add_ingredient(buns_with_ingred[1][0])
        # Если булка не установлена — цена равна сумме ингредиентов (или 0)
        assert burger.get_price() == buns_with_ingred[1][0].get_price()

    # Проверка чека, если булка не установлена
    def test_get_receipt_without_bun(self, buns_with_ingred):
        burger = Burger()
        burger.add_ingredient(buns_with_ingred[1][0])
        # Проверяем чек без булки — в зависимости от реализации
        expected_receipt = BunsWithIngred.get_my_receipt(None, [buns_with_ingred[1][0]])
        assert burger.get_receipt() == expected_receipt
