import allure

from praktikum.ingredient import Ingredient
from data import TestAnotherIngredientData, TestReceiptData

class TestBurger:
    @allure.title("Проверка дефолтного бургера ")
    def test_burger_initial(self, test_burger):
        assert test_burger.bun is None
        assert isinstance(test_burger.ingredients, list) and len(test_burger.ingredients) == 0

    @allure.title("Добавление булки для бургера")
    def test_set_buns(self, test_burger, test_bun):
        test_burger.set_buns(test_bun)
        assert test_burger.bun is test_bun

    @allure.title("Добавление начинки в бургер")
    def test_add_ingredient(self, test_burger, test_ingredient):
        test_burger.add_ingredient(test_ingredient)
        assert test_ingredient in test_burger.ingredients

    @allure.title("Удаление ингридиента из бургера")
    def test_remove_ingredient(self, test_burger, test_ingredient):
        test_burger.add_ingredient(test_ingredient)
        index = test_burger.ingredients.index(test_ingredient)
        test_burger.remove_ingredient(index)
        assert test_ingredient not in test_burger.ingredients

    @allure.title("Перемещение ингридиента в бургере")
    def test_move_ingredient(self, test_burger, test_ingredient):
        another_test_ingredient = Ingredient(
            TestAnotherIngredientData.ingredient_type, TestAnotherIngredientData.name, TestAnotherIngredientData.price
        )
        test_burger.add_ingredient(another_test_ingredient)
        test_burger.add_ingredient(test_ingredient)
        index = test_burger.ingredients.index(test_ingredient)
        test_burger.move_ingredient(index, 0)
        new_index = test_burger.ingredients.index(test_ingredient)
        assert new_index == 0

    @allure.title("Получение цены бургера с ингредиентами")
    def test_get_price(self, test_burger, test_bun, test_ingredient):
        test_burger.set_buns(test_bun)
        test_burger.add_ingredient(test_ingredient)
        another_test_ingredient = Ingredient(
            TestAnotherIngredientData.ingredient_type, TestAnotherIngredientData.name, TestAnotherIngredientData.price
        )
        test_burger.add_ingredient(another_test_ingredient)
        assert test_burger.get_price() == 610.0

    @allure.title("Получение чека на бургер")
    def test_get_receipt(self, test_burger, test_bun, test_ingredient):
        test_burger.set_buns(test_bun)
        test_burger.add_ingredient(test_ingredient)
        another_test_ingredient = Ingredient(
            TestAnotherIngredientData.ingredient_type, TestAnotherIngredientData.name, TestAnotherIngredientData.price
        )
        test_burger.add_ingredient(another_test_ingredient)
        assert test_burger.get_receipt() == TestReceiptData.receipt


