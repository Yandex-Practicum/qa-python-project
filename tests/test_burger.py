import pytest 
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import BunData, IngredientData
from unittest.mock import Mock
#python -B -m pytest tests/test_burger.py

class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        bun = Bun(*BunData.black_bun)
        burger.set_buns(bun)
        assert burger.bun == bun

    @pytest.mark.parametrize(
    "ingredient_sample",
    [
        IngredientData.hot_sauce,
        IngredientData.sour_cream,
        IngredientData.chili_sauce,
        IngredientData.cutlet,
        IngredientData.dinousaur,
        IngredientData.sausage
    ])
    def test_add_ingredient(self, ingredient_sample):
        burger = Burger()
        ingredient = Ingredient(*ingredient_sample)
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient_1 = Ingredient(*IngredientData.hot_sauce)
        ingredient_2 = Ingredient(*IngredientData.sausage)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.remove_ingredient(0)
        assert burger.ingredients == [ingredient_2]

    def test_move_ingredient(self):
        burger = Burger()
        ingredient_1 = Ingredient(*IngredientData.hot_sauce)
        ingredient_2 = Ingredient(*IngredientData.sausage)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_2, ingredient_1]

    @pytest.mark.parametrize(
    "bun_name, bun_price, ingredient_1_sample, ingredient_2_sample",
    [(
        BunData.black_bun[0], 
        BunData.black_bun[1],
        IngredientData.hot_sauce,
        IngredientData.sausage

    )])
    def test_get_price_with_bun_and_ingredients(self, bun_name, bun_price, ingredient_1_sample, ingredient_2_sample):
        burger = Burger()
        bun = Bun(bun_name, bun_price)
        burger.set_buns(bun)
        ingredient_1 = Ingredient(*ingredient_1_sample)
        ingredient_2 = Ingredient(*ingredient_2_sample)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        assert burger.get_price() == bun_price*2+ingredient_1_sample[2]+ingredient_2_sample[2]

    @pytest.mark.parametrize(
    "bun_name, bun_price, ingredient_1_sample",
    [(
        BunData.black_bun[0], 
        BunData.black_bun[1],
        IngredientData.sausage

    )])
    def test_get_receipt(self, bun_name, bun_price, ingredient_1_sample):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = bun_price

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ingredient_1_sample[0]
        mock_ingredient.get_name.return_value = ingredient_1_sample[1]
        mock_ingredient.get_price.return_value = ingredient_1_sample[2]
        
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]

        price = bun_price*2+ingredient_1_sample[2]
        receipt = burger.get_receipt()

        assert bun_name in receipt
        assert ingredient_1_sample[1] in receipt
        assert f'Price: {price}' in receipt