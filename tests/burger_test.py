from unittest.mock import patch

from data import Data
from praktikum.burger import Burger


class TestBurger:
    def test_create_burger(self):
        burger = Burger()
        assert burger.bun is None and burger.ingredients == []

    @patch('praktikum.bun.Bun')
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @patch('praktikum.ingredient.Ingredient')
    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1 and burger.ingredients[0] == mock_ingredient

    @patch('praktikum.ingredient.Ingredient')
    def test_remove_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.ingredients.append(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    @patch('praktikum.ingredient.Ingredient')
    @patch('praktikum.ingredient.Ingredient')
    def test_move_ingredient(self, mock_ingredient1, mock_ingredient2):
        burger = Burger()
        burger.ingredients.append(mock_ingredient1)
        burger.ingredients.append(mock_ingredient2)
        burger.move_ingredient(0,1)
        assert burger.ingredients[0] == mock_ingredient2 and burger.ingredients[1] == mock_ingredient1

    @patch('praktikum.ingredient.Ingredient')
    @patch('praktikum.ingredient.Ingredient')
    @patch('praktikum.bun.Bun')
    def test_get_price(self, mock_ingredient1, mock_ingredient2, mock_bun):
        burger = Burger()

        #настраиваем моки
        mock_bun.get_price.return_value = 3.1
        mock_ingredient1.get_price.return_value = 2.2
        mock_ingredient2.get_price.return_value = 4.4


        #добавляем булку и ингредиенты
        burger.bun = mock_bun
        burger.ingredients.append(mock_ingredient1)
        burger.ingredients.append(mock_ingredient2)


        actual_price = burger.get_price()
        expected_price = (3.1 * 2) + 2.2 + 4.4

        assert actual_price == expected_price and isinstance(actual_price, float)

    @patch('praktikum.ingredient.Ingredient')
    @patch('praktikum.bun.Bun')
    def test_get_receipt(self, mock_ingredient, mock_bun):
        burger = Burger()

        #настраиваем моки
        mock_bun.get_name.return_value = "Призрачная булка"
        mock_bun.get_price.return_value = 3.1
        mock_ingredient.get_type.return_value = "Основная начинка"
        mock_ingredient.get_name.return_value = "Бекон"
        mock_ingredient.get_price.return_value = 2.2

        #добавляем булку и ингредиенты
        burger.bun = mock_bun
        burger.ingredients.append(mock_ingredient)

        actual_receipt = burger.get_receipt()
        expected_receipt = Data.RECEIPT

        assert actual_receipt == expected_receipt


