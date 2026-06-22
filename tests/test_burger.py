import pytest
import allure
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@allure.epic("Stellar Burgers")
@allure.feature("Юнит-тесты компонентов бургера")
class TestBurger:
    @allure.title("Установка булочек для бургера")
    def test_set_buns_mock_bun_sets_bun_variable(self):
        burger = Burger()
        mock_bun = Mock()

        with allure.step("Установить мок-булочку в объект бургера"):
            burger.set_buns(mock_bun)
        with allure.step("Проверить что булочка успешно сохранена в бургере"):
            assert burger.bun == mock_bun

    @allure.title("Добавление ингридиента в бургер")
    @pytest.mark.parametrize("ingredient_type", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_add_ingredient_mock_ingredient_adds_to_list(self,ingredient_type):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ingredient_type

        with allure.step(f"Добавить ингредиент типа {ingredient_type} в бургер"):
            burger.add_ingredient(mock_ingredient)
        
        with allure.step("Проверить, что список ингредиентов содержит ровно 1 элемент"):
            assert len(burger.ingredients) == 1
            assert burger.ingredients[0] == mock_ingredient

    @allure.title("Удаление ингридиента из бургера")
    def test_remove_ingredient_populated_list_removes_from_list(self):
        burger = Burger()
        mock_ingredient = Mock()
        with allure.step("Добавить ингредиент в бургер"):
            burger.add_ingredient(mock_ingredient)
       
        with allure.step("Удалить ингредиент по индексу 0"):
            burger.remove_ingredient(0)
        with allure.step("Проверить, что список ингредиентов стал пустым"):
            assert len(burger.ingredients) == 0

    @allure.title("Перемещение ингридиента на другую позицию в рецепте")
    def test_move_ingredient_populated_list_changes_position(self):
        burger = Burger()
        mock_ing_1 = Mock()
        mock_ing_2 = Mock()
        burger.add_ingredient(mock_ing_1)
        burger.add_ingredient(mock_ing_2)
        
        with allure.step("Переместить ингредиент с индекса 0 на индекс 1"):
            burger.move_ingredient(0, 1)

        with allure.step("Проверить, что ингредиенты поменялись местами"):
            assert burger.ingredients[0] == mock_ing_2
            assert burger.ingredients[1] == mock_ing_1

    @allure.title("Расчет финальной соимости бургера")
    def test_get_price_mock_bun_and_ingredients_returns_total_sum(self):
        burger =Burger()
        
        with allure.step("Создать мок булочки с ценой 100"):
            mock_bun = Mock()
            mock_bun.get_price.return_value = 100.0

        with allure.step("Создать мок соуса/начинки с ценой 50"):
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = 50.0
            
            burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        
        with allure.step("Проверить итоговый расчет стоимости: (100 * 2) + 50 = 250"):
            assert burger.get_price() == 250.0

    @allure.title("Генерация текстового чека для заказа")
    def test_get_receipt_mock_bun_and_ingredients_returns_formatted_receipt(self):
        burger = Burger()
        
        with allure.step("Настроить мок для булочки (название и цена)"):
            mock_bun = Mock()
            mock_bun.get_name.return_value = "Флюоресцентная булка"
            mock_bun.get_price.return_value = 100.0
        
        with allure.step("Настроить мок для ингредиента (тип, название и цена)"):
            mock_ingredient = Mock()
            mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
            mock_ingredient.get_name.return_value = "Соус Spicy"
            mock_ingredient.get_price.return_value = 50.0
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        
        with allure.step("Сгенерировать чек"):
            receipt = burger.get_receipt()
        
        with allure.step("Убедиться, что все элементы бургера и финальная цена попали в структуру чека"):
            assert "(==== Флюоресцентная булка ====)" in receipt
            assert "= sauce Соус Spicy =" in receipt
            assert "Price: 250" in receipt

