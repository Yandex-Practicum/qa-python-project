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

    def test_remove_ingredient(self, burger):
        ingredient_ketchup = Ingredient("Соус", "Кетчуп", 10.0)
        burger.add_ingredient(ingredient_ketchup)
        ingredient_cheese = Ingredient("Начинка", "Сыр", 20.0)
        burger.add_ingredient(ingredient_cheese)
        ingr_list_len_2 = len(burger.ingredients)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1 and ingr_list_len_2 == 2 and burger.ingredients[0].get_name() == ingredient_cheese.get_name()

    def test_move_ingredient(self, burger):
        ingredient_ketchup = Ingredient("Соус", "Кетчуп", 10.0)
        burger.add_ingredient(ingredient_ketchup)
        ingredient_cheese = Ingredient("Начинка", "Сыр", 20.0)
        burger.add_ingredient(ingredient_cheese)
        ingr_list_before = [burger.ingredients[0].get_name(), burger.ingredients[1].get_name()]
        burger.move_ingredient(0, 1)
        assert ingr_list_before[0] == burger.ingredients[1].get_name() and ingr_list_before[1] == burger.ingredients[0].get_name()

    @patch('praktikum.ingredient.Ingredient.get_price', return_value = 60.0)
    @patch('praktikum.bun.Bun.get_price', return_value = 35.0)
    def test_get_price(self, mock_bun, mock_ingredient, burger, ingredient, bun):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == 250.0

    @patch('praktikum.burger.Burger.get_price', return_value = 100.0)
    @patch('praktikum.ingredient.Ingredient.get_type', return_value = "Начинка")
    @patch('praktikum.ingredient.Ingredient.get_name', return_value = "Сало")
    @patch('praktikum.bun.Bun.get_name', return_value = "Бородинская")
    def test_get_receipt(self, mock_bun, mock_ingr_name, mock_ingr_type, mock_get_price, burger, ingredient, bun):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient)
        assert data.RECEIPT == burger.get_receipt()
