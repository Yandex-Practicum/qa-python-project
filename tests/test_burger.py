import pytest
import allure
from unittest.mock import MagicMock
from prakticum.ingredient import Ingredient



class TestBurger:
    @allure.title("Тест на установку булочки")
    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @allure.title("Тест на добавление ингредиента")
    def test_add_ingredient(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    @allure.title("Тест на удаление ингредиента")
    def test_remove_ingredient(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0


    @allure.title("Тест на перемещение ингредиента")
    def test_move_ingredient(self, burger, mock_bun, mock_ingredient):
        ingredient2 = MagicMock(spec=Ingredient)
        ingredient2.get_name.return_value = 'Lettuce'
        ingredient2.get_price.return_value = 0.5
        ingredient2.get_type.return_value = 'Vegetable'

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(ingredient2)

        burger.move_ingredient(1, 0)

        assert burger.ingredients[0] == ingredient2
        assert burger.ingredients[1] == mock_ingredient


    @allure.title("Тест на расчет цены")
    def test_get_price(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        expected_price = 2.5 * 2 + 1.0
        assert burger.get_price() == expected_price

    @allure.title("Тест на получение чека")
    def test_get_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        expected_receipt = (
            '(==== Sesame Bun ====)\n'
            '= cheese Cheese =\n'
            '(==== Sesame Bun ====)\n'
            '\n'
            'Price: 6.0'
        )
        assert burger.get_receipt() == expected_receipt


    @allure.title("Тест на добавление нескольких ингредиентов")
    def test_add_multiple_ingredients(self, burger, mock_bun, multiple_ingredients):
        burger.set_buns(mock_bun)
        for ingredient in multiple_ingredients:
            burger.add_ingredient(ingredient)

        assert len(burger.ingredients) == 3
        expected_price = 2.5 * 2 + 1.0 + 0.5 + 0.7
        assert burger.get_price() == expected_price

    @allure.title("Тест на чек с несколькими ингредиентами")
    def test_get_receipt_with_multiple_ingredients(self, burger, mock_bun, multiple_ingredients):
        burger.set_buns(mock_bun)
        for ingredient in multiple_ingredients:
            burger.add_ingredient(ingredient)

        expected_receipt = (
            '(==== Sesame Bun ====)\n'
            '= cheese Cheese =\n'
            '= vegetable Lettuce =\n'
            '= vegetable Tomato =\n'
            '(==== Sesame Bun ====)\n'
            '\n'
            'Price: 7.2'
        )
        assert burger.get_receipt() == expected_receipt


    @allure.title("Тест на добавление пустого ингредиента")
    def test_add_empty_ingredient(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        empty_ingredient = MagicMock(spec=Ingredient)
        empty_ingredient.get_name.return_value = None
        empty_ingredient.get_price.return_value = 0.0
        burger.add_ingredient(empty_ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == empty_ingredient


    @allure.title("Тест на добавление большого количества ингредиентов")
    def test_add_large_number_of_ingredients(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        for i in range(50):
            ingredient = MagicMock(spec=Ingredient)
            ingredient.get_name.return_value = f'Ingredient {i}'
            ingredient.get_price.return_value = 0.5
            burger.add_ingredient(ingredient)

        assert len(burger.ingredients) == 50
        assert burger.get_price() == 2.5 * 2 + 50 * 0.5


    @allure.title("Тест на удаление ингредиента по неверному индексу")
    def test_remove_ingredient_invalid_index(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        with pytest.raises(IndexError):
            burger.remove_ingredient(10)


    @allure.title("Проверка добавления недопустимого ингредиента")
    def test_add_invalid_ingredient_type(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        invalid_ingredient = MagicMock()
        burger.add_ingredient(invalid_ingredient)
        assert len(burger.ingredients) == 1

    @allure.title("Тест на расчет цены без булочки")
    def test_get_price_without_bun(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        with pytest.raises(AttributeError):
            burger.get_price()


    @allure.title("Тест на генерацию чека без булочки")
    def test_get_receipt_without_bun(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        with pytest.raises(AttributeError):
            burger.get_receipt()


    @allure.title("Тест на пустой бургер (только булочка)")
    def test_empty_burger(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.get_price() == 2.5 * 2
        expected_receipt = (
            '(==== Sesame Bun ====)\n'
            '(==== Sesame Bun ====)\n'
            '\n'
            'Price: 5.0'
        )
        assert burger.get_receipt() == expected_receipt


    @allure.title("Тест на добавление дублированных ингредиентов")
    def test_duplicate_ingredients(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 2
        assert burger.get_price() == 2.5 * 2 + 1.0 * 2


    @allure.title("Тест на тип возвращаемого значения цены")
    def test_get_price_type(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert isinstance(burger.get_price(), float)


    @allure.title("Тест на тип возвращаемого значения чека")
    def test_get_receipt_type(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert isinstance(burger.get_receipt(), str)


    @allure.title("Проверяем, что None корректно устанавливается как булочка")
    def test_set_none_bun(self, burger):
        burger.set_buns(None)
        assert burger.bun is None


    @allure.title("Проверяем обработку None ингредиента")
    def test_add_none_ingredient(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        burger.add_ingredient(None)
        assert None in burger.ingredients



