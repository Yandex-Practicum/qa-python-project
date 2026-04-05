from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

from unittest.mock import Mock
import pytest



class TestBurgerInitialization:

    # ИСПРАВЛЕННЫЙ ТЕСТ 1: Проверяем set_buns через влияние на цену
    def test_set_bun_calculates_price_correctly(self, burger_instance, mock_bun):
        # Arrange: mock_bun имеет цену 1000 (из фикстуры)
        burger_instance.set_buns(mock_bun)
        # Если булка установилась верно, цена должна быть 1000 * 2 = 2000.
        # Если бы булка не установилась, метод get_price() упал бы с ошибкой (AttributeError).
        assert burger_instance.get_price() == 2000


    # Тест 2 НОВЫЙ: Проверяем поведение метода add_ingredient через изменение цены
    def test_add_ingredient_increases_price(self, burger_instance, mock_bun, mock_ingredient):
        # Устанавливаем булку, чтобы цена считалась корректно (иначе будет ошибка или 0)
        burger_instance.set_buns(mock_bun)
        # Цена булки 1000 (из фикстуры), значит база = 2000.
        # Цена ингредиента 50 (из фикстуры). Ожидаемый итог: 2050.
        expected_price = 2050 
        # Добавляем ингредиент
        burger_instance.add_ingredient(mock_ingredient)
        # Проверяем результат через публичный метод get_price()
        assert burger_instance.get_price() == expected_price


    # Тест 3 НОВЫЙ: Проверяем поведение метода add_ingredient формирование чека
    def test_add_ingredient_appears_in_receipt(self, burger_instance, mock_bun, mock_ingredient):
        # Устанавливаем булку
        burger_instance.set_buns(mock_bun)
        # Добавляем ингредиент
        burger_instance.add_ingredient(mock_ingredient)
        # Получаем чек
        receipt = burger_instance.get_receipt()
        # Проверяем, что имя ингредиента есть в чеке
        # Мы знаем из фикстуры, что имя "Test Ingredient Name"
        assert "Test Ingredient Name" in receipt
        
    
    
class TestBurgerManipulation:

    # Тест 1 : Позитивный сценарий удаления ингредиента (проверка через изменение цены)
    def test_remove_ingredient_decreases_price(self, burger_instance, mock_bun, mock_ingredient, mock_two_ingredient):
        # Подготовка данных
        # Из фикстур знаем: 
        # mock_ingredient price = 50
        # mock_two_ingredient price = 70
        burger_instance.set_buns(mock_bun) # Цена булки 1000 -> база 2000
        burger_instance.add_ingredient(mock_ingredient)      # +50 -> 2050
        burger_instance.add_ingredient(mock_two_ingredient) # +70 -> 2120
        # Удаляем первый ингредиент (тот, что стоит 50)
        burger_instance.remove_ingredient(0)
        # Проверяем поведение через цену
        # Ожидаемая цена: 2125 - 50 = 2070
        expected_price_after_remove = 2070
        assert burger_instance.get_price() == expected_price_after_remove


    # Тест 2: Удаление (Негативный / Ошибка)
    def test_remove_ingredient_raises_error_on_invalid_index(self, burger_instance, mock_ingredient):
        burger_instance.add_ingredient(mock_ingredient)
        with pytest.raises(IndexError):
           burger_instance.remove_ingredient(99)

    # ИСПРАВЛЕННЫЙ ТЕСТ 3: Проверяем move_ingredient через порядок в чеке
    def test_move_ingredient_changes_order_in_receipt(self, burger_instance, mock_ingredient_a, mock_ingredient_b, mock_ingredient_c, mock_bun):
        # Берём данные из фикстуры (3 мока)
        burger_instance.set_buns(mock_bun)
        burger_instance.add_ingredient(mock_ingredient_a) # Порядок: A, B, C
        burger_instance.add_ingredient(mock_ingredient_b)
        burger_instance.add_ingredient(mock_ingredient_c)
        # Перемещаем A (индекс 0) в конец (индекс 2). Ожидаемый порядок: B, C, A
        burger_instance.move_ingredient(0, 2)
        # Получаем чек и проверяем порядок следования имен в строке
        receipt = burger_instance.get_receipt()
        # Находим индексы вхождений имен в строку чека
        pos_a = receipt.find("Ingredient_A")
        pos_b = receipt.find("Ingredient_B")
        pos_c = receipt.find("Ingredient_C")
        # Проверяем, что все найдены и порядок верный: B идет раньше C, C раньше A
        assert pos_b < pos_c < pos_a


    # Тест 4: Перемещение (Негативный / Ошибка)
    def test_move_ingredient_raises_error_on_invalid_index(self, burger_instance, mock_ingredient):
        burger_instance.add_ingredient(mock_ingredient)
        with pytest.raises(IndexError):
            burger_instance.move_ingredient(5, 0)


class TestBurgerPrice:

    @pytest.mark.parametrize("bun_price, ingredient_prices, expected_total", [
    (100, [], 200),
    (150, [50], 350),
    (200, [10, 20], 430),])

    def test_get_price_calculation(self, burger_instance, bun_price, ingredient_prices, expected_total):
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        mock_bun.get_name.return_value = "Test Bun" 
        burger_instance.set_buns(mock_bun)
        for price in ingredient_prices:
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = price
            mock_ingredient.get_type.return_value = "FILLING"
            mock_ingredient.get_name.return_value = "Test Ingredient"
            burger_instance.add_ingredient(mock_ingredient)
        actual_price = burger_instance.get_price()
        assert actual_price == expected_total


class TestBurgerReceipt:


    @pytest.mark.parametrize("bun_name, ing_type, ing_name, expected_ing_type_lower",[
    ('White Bun', "FILLING", "Meat Ball", "filling" ),
    ("Black Bun", "SAUCE", "Hot Sauce", "sauce"),
    ("Red Bun", "SaUcE", "Ketchup","sauce"),
    ])
    def test_get_receipt_format(self, burger_instance, bun_name, ing_name, ing_type, expected_ing_type_lower):
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = 1500

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ing_type
        mock_ingredient.get_name.return_value =  ing_name
        mock_ingredient.get_price.return_value = 420

        expected_price = (1500*2) + 420

        burger_instance.set_buns(mock_bun)
        burger_instance.add_ingredient(mock_ingredient)
        expected_receipt = f"(==== {bun_name} ====)\n= {expected_ing_type_lower} {ing_name} =\n(==== {bun_name} ====)\n\nPrice: {expected_price}"
        actual_receipt = burger_instance.get_receipt()
        assert actual_receipt == expected_receipt
