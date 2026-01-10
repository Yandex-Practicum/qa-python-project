from burger import Burger
from data import Data
import allure

class TestBurger:
    @allure.title('Добавление булочек')
    @allure.description('Проверка добавления булочек бургера через метод set_buns')
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    @allure.title('Проверка добавления ингредиента')
    @allure.description('Проверка добавления ингредиента через метод add_ingredient')
    def test_add_ingredient_mocks_got_added(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)

        assert mock_ingredient in burger.ingredients and len(burger.ingredients) == 2

    @allure.title('Удаления ингредиента')
    @allure.description('Проверка удаления ингредиента через метод remove_ingredient')
    def test_remove_ingredient_mocks_ingredient_removed(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(1)

        assert mock_bun in burger.ingredients and mock_ingredient not in burger.ingredients

    @allure.title('Перемещение ингредиентов')
    @allure.description('Проверка перемещения ингредиенты внутри бургера через метод move_ingredient')
    def test_move_mocks_ingredients_got_moved(self, mock_bun, mock_ingredient):
        mock_bun.name = Data.BUN_NAME_MOCKED
        burger = Burger()
        burger.add_ingredient(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.move_ingredient(1, 0)

        assert burger.ingredients[0] == mock_ingredient and burger.ingredients[1] == mock_bun

    @allure.title('Цена бургера')
    @allure.description('Проверка получения цена бургера через метод get_price')
    def test_get_price_mocks_success(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        price = mock_bun.get_price() * 2 + mock_ingredient.get_price()

        assert burger.get_price() == price

    @allure.title("Рецепт бургера")
    @allure.description('Проверка получения рецепта бургера через метод get_receipt')
    def test_get_receipt_mocks_success(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
