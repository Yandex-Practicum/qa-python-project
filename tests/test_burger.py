import allure
import pytest
from unittest.mock import Mock
from bun import Bun
from ingredient import Ingredient
from burger import Burger

@allure.suite('Тесты класса "burger"')
class TestBurger:

    @allure.title('Проверка создания бургера')
    def test_init_correct_burger(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    @allure.title("Проверка создания булки")
    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @allure.title("Проверка добавления ингредиента в бургер")
    def test_add_ingredient_success(self):
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_name.return_value = "cheese"
        mock_ingredient.get_price.return_value = 150.0
        mock_ingredient.get_type.return_value = "FILLING"
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    @allure.title('Проверка добавления ингредиента')
    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient2 = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredient2
        assert burger.ingredients[1] == mock_ingredient1

    @allure.title('Удаление ингридиентов')
    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient2 = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient2

    @allure.title('Расчет цены бургера')
    def test_get_price_with_bun_and_ingredients(self):
        burger = Burger()

        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 100.0

        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_price.return_value = 150.0

        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_price.return_value = 200.0

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        expected_price = (100 * 2) + 150 + 200
        assert burger.get_price() == expected_price

    @allure.title('Расчет чека для булочки')
    def test_get_receipt_only_bun(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        expected_receipt = (
            "(==== black bun ====)\n"
            "(==== black bun ====)\n\n"
            "Price: 200.0"
        )
        assert receipt == expected_receipt





