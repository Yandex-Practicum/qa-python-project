from unittest.mock import Mock
import allure
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient



class TestBurger:
    @allure.title('проверка конструктора')
    def test_burger_creation(self):
        burger = Burger()
        assert burger.bun is None
        assert len(burger.ingredients) == 0

    @allure.title('проверка что можно установить булку')
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @allure.title('проверка что можно добавить ингредиент')
    def test_add_ingredient(self, mock_ingredients_sauce):
        burger = Burger()
        burger.add_ingredient(mock_ingredients_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredients_sauce

    @allure.title('проверка удаления одного ингредиента')
    def test_remove_ingredient(self, mock_ingredients_sauce, mock_ingredients_sauce_filling):
        burger = Burger()
        burger.add_ingredient(mock_ingredients_sauce)
        burger.add_ingredient(mock_ingredients_sauce_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredients_sauce_filling

    @allure.title('проверка перемещения ингредиента')
    def test_move_ingredient(self, mock_ingredients_sauce, mock_ingredients_sauce_filling):
        burger = Burger()
        burger.add_ingredient(mock_ingredients_sauce)
        burger.add_ingredient(mock_ingredients_sauce_filling)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == mock_ingredients_sauce_filling
        assert burger.ingredients[1] == mock_ingredients_sauce

    @allure.title('проверка получения цены')
    def test_get_price(self, mock_ingredients_sauce, mock_ingredients_sauce_filling, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        mock_ingredient1 = Mock(Ingredient)
        mock_ingredient1.get_price.return_value = 0.5
        mock_ingredient2 = Mock(Ingredient)
        mock_ingredient2.get_price.return_value = 1.0
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        assert burger.get_price() == 4.5

    @allure.title('проверка получение чека')
    def test_get_receipt(self, mock_ingredients_sauce, mock_ingredients_sauce_filling, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredients_sauce)
        burger.add_ingredient(mock_ingredients_sauce_filling)
        expected_receipt = ('(==== Sesame ====)\n'
                            '= sauce ketchup =\n'
                            '= filling cheese =\n'
                            '(==== Sesame ====)\n'
                            '\n'
                            'Price: 4.5')
        assert burger.get_receipt() == expected_receipt
