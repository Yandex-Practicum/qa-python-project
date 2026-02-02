import allure
from data import Data
from praktikum.burger import Burger


class TestBurger:

    @allure.title('Проверка установки булок')
    @allure.description('Проверяем, что можно установить булки методом set_buns')
    def test_set_buns(self, mock_bun):
        mock_bun.name = Data.MOCK_BUN_NAME
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    @allure.title('Проверка добавления ингредиента')
    @allure.description('Проверяем, что можно добавить ингредиент методом add_ingredient')
    def test_add_ingredient(self, mock_ingredient):
        mock_ingredient.name = Data.MOCK_INGREDIENT_NAME
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert mock_ingredient in burger.ingredients and len(burger.ingredients) == 1

    @allure.title('Проверка удаления добавленного ингредиента')
    @allure.description('Проверяем, что можно удалять ингредиент методом remove_ingredient')
    def test_remove_ingredient(self, mock_bun, mock_ingredient):
        mock_bun.name = Data.MOCK_BUN_NAME
        mock_ingredient.name = Data.MOCK_INGREDIENT_NAME
        burger = Burger()
        burger.add_ingredient(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert mock_ingredient in burger.ingredients and mock_bun not in burger.ingredients and len(
            burger.ingredients) == 1

    @allure.title('Проверка перемещения местами ингредиентов')
    @allure.description('Проверяем, что можно менять местами добавленные ингредиенты методом move_ingredient')
    def test_move_ingredient(self, mock_bun, mock_ingredient):
        mock_bun.name = Data.MOCK_BUN_NAME
        mock_ingredient.name = Data.MOCK_INGREDIENT_NAME
        burger = Burger()
        burger.add_ingredient(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.move_ingredient(1, 0)

        assert burger.ingredients[0] == mock_ingredient and burger.ingredients[1] == mock_bun

    @allure.title('Проверка получения цены бургера')
    @allure.description('Проверяем, что можно получить цену бургера с добавленными ингредиентами методом get_price')
    def test_get_price(self, mock_bun, mock_ingredient):
        mock_bun.get_name.return_value = Data.MOCK_BUN_NAME
        mock_bun.get_price.return_value = Data.MOCK_BUN_PRICE
        mock_ingredient.get_name.return_value = Data.MOCK_INGREDIENT_NAME
        mock_ingredient.get_price.return_value = Data.MOCK_INGREDIENT_PRICE
        mock_ingredient.get_type.return_value = Data.MOCK_INGREDIENT_TYPE
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        price = (mock_bun.get_price() * 2) + mock_ingredient.get_price()

        assert burger.get_price() == price

    @allure.title("Проверка отображения рецепта")
    @allure.description('Проверяем, что можно получить рецепт бургера с добавленными ингредиентами методом get_receipt')
    def test_get_receipt(self, mock_bun, mock_ingredient):
        mock_bun.get_name.return_value = Data.MOCK_BUN_NAME
        mock_bun.get_price.return_value = Data.MOCK_BUN_PRICE
        mock_ingredient.get_name.return_value = Data.MOCK_INGREDIENT_NAME
        mock_ingredient.get_price.return_value = Data.MOCK_INGREDIENT_PRICE
        mock_ingredient.get_type.return_value = Data.MOCK_INGREDIENT_TYPE
        
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()

        expected_price = (Data.MOCK_BUN_PRICE * 2) + Data.MOCK_INGREDIENT_PRICE
        ingredient_type_lower = Data.MOCK_INGREDIENT_TYPE.lower()
        expected_price_formatted = f'{expected_price:.1f}'
        
        assert receipt == (f'(==== {Data.MOCK_BUN_NAME} ====)\n'
                           f'= {ingredient_type_lower} {Data.MOCK_INGREDIENT_NAME} =\n'
                           f'(==== {Data.MOCK_BUN_NAME} ====)\n'
                           f'\n'
                           f'Price: {expected_price_formatted}')