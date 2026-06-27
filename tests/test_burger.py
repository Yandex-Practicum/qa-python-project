import data
from unittest.mock import patch
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from typing import List


class TestBurger:
    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert isinstance(burger.bun, Bun) and burger.bun.get_name() == data.BUN_NAME

    def test_add_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        assert isinstance(burger.ingredients, List) and isinstance(burger.ingredients[0], Ingredient) and burger.ingredients[0].get_name() == data.INGR_NAME

    def test_remove_ingredient(self, burger, mock_ingredient):
        mock_ingredient.configure_mock(type="Соус")
        mock_ingredient.configure_mock(name="Кетчуп")
        mock_ingredient.configure_mock(price=10.0)

        mock_ingredient_ketchup = mock_ingredient

        burger.add_ingredient(mock_ingredient_ketchup)

        mock_ingredient.configure_mock(type="Начинка")
        mock_ingredient.configure_mock(name="Сыр")
        mock_ingredient.configure_mock(price=20.0)
        mock_ingredient.get_name.return_value = "Сыр"

        mock_ingredient_cheese = mock_ingredient

        burger.add_ingredient(mock_ingredient_cheese)

        ingr_list_len_2 = len(burger.ingredients)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1 and ingr_list_len_2 == 2 and burger.ingredients[0].get_name() == mock_ingredient_cheese.get_name()

    def test_move_ingredient(self, burger, mock_ingredient):
        mock_ingredient.configure_mock(type="Соус")
        mock_ingredient.configure_mock(name="Кетчуп")
        mock_ingredient.configure_mock(price=10.0)
        mock_ingredient.get_name.return_value = "Кетчуп"

        mock_ingredient_ketchup = mock_ingredient

        burger.add_ingredient(mock_ingredient_ketchup)

        mock_ingredient.configure_mock(type="Начинка")
        mock_ingredient.configure_mock(name="Сыр")
        mock_ingredient.configure_mock(price=20.0)
        mock_ingredient.get_name.return_value = "Сыр"

        mock_ingredient_cheese = mock_ingredient

        burger.add_ingredient(mock_ingredient_cheese)

        ingr_list_before = [burger.ingredients[0].get_name(), burger.ingredients[1].get_name()]
        burger.move_ingredient(0, 1)

        assert ingr_list_before[0] == burger.ingredients[1].get_name() and ingr_list_before[1] == burger.ingredients[0].get_name()

    def test_get_price(self, burger, mock_ingredient, mock_bun):
        mock_bun.get_price.return_value = 35.0
        mock_ingredient.get_price.return_value = 60.0

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == 250.0

    @patch('praktikum.burger.Burger.get_price', return_value = 100.0)
    def test_get_receipt(self, mock_burg_get_price, burger, mock_ingredient, mock_bun):
        mock_bun.get_name.return_value = data.RECEIPT_BUN_NAME
        mock_ingredient.get_name.return_value = data.RECEIPT_INGR_NAME
        mock_ingredient.get_type.return_value = data.RECEIPT_INGR_TYPE

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        
        assert data.RECEIPT == burger.get_receipt()
