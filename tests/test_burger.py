import pytest
from unittest.mock import Mock, patch
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
 
 
    def setup_method(self):
    
        self.burger = Burger()
        self.mock_bun = Mock(spec=Bun)
        self.mock_ingredient1 = Mock(spec=Ingredient)
        self.mock_ingredient2 = Mock(spec=Ingredient)

    def test_init(self):
 
        assert self.burger.bun is None
        assert self.burger.ingredients == []

    def test_set_buns(self):

        self.burger.set_buns(self.mock_bun)
        assert self.burger.bun == self.mock_bun

    def test_add_ingredient(self):

        self.burger.add_ingredient(self.mock_ingredient1)
        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0] == self.mock_ingredient1

        self.burger.add_ingredient(self.mock_ingredient2)
        assert len(self.burger.ingredients) == 2
        assert self.burger.ingredients[1] == self.mock_ingredient2

    def test_remove_ingredient(self):

        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        assert len(self.burger.ingredients) == 2

        self.burger.remove_ingredient(0)
        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0] == self.mock_ingredient2

    def test_remove_ingredient_invalid_index(self):
  
        self.burger.add_ingredient(self.mock_ingredient1)

        with pytest.raises(IndexError):
            self.burger.remove_ingredient(5)

    @pytest.mark.parametrize("index, new_index", [
        (0, 1),
        (1, 0),  
        (0, 0),  
    ])
    def test_move_ingredient(self, index, new_index):

        
        mock_ing1 = Mock(spec=Ingredient)
        mock_ing2 = Mock(spec=Ingredient)
        mock_ing1.get_name.return_value = "ingredient1"
        mock_ing2.get_name.return_value = "ingredient2"
        
        self.burger.ingredients = [mock_ing1, mock_ing2]

        self.burger.move_ingredient(index, new_index)

        
        assert len(self.burger.ingredients) == 2

    def test_move_ingredient_invalid_index(self):

        self.burger.add_ingredient(self.mock_ingredient1)

        with pytest.raises(IndexError):
            self.burger.move_ingredient(2, 0)

    @pytest.mark.parametrize("bun_price, ingredient_prices, expected_price", [
        (100, [50, 75], 325), 
        (200, [100, 150, 200], 850), 
        (50, [], 100), 
    ])
    def test_get_price(self, bun_price, ingredient_prices, expected_price):
        
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = bun_price
        self.burger.set_buns(mock_bun)

        for price in ingredient_prices:
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_price.return_value = price
            self.burger.add_ingredient(mock_ingredient)

        assert self.burger.get_price() == expected_price

    def test_get_price_no_bun(self):

        with pytest.raises(AttributeError):
            self.burger.get_price()

    def test_get_receipt_without_ingredients(self):
   
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "red bun"
        mock_bun.get_price.return_value = 100
        self.burger.set_buns(mock_bun)

        receipt = self.burger.get_receipt()
        
        expected_receipt = "(==== red bun ====)\n(==== red bun ====)\n\nPrice: 200"
        assert receipt == expected_receipt

    def test_get_receipt_with_one_ingredient(self):
    
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "white bun"
        mock_bun.get_price.return_value = 100
        self.burger.set_buns(mock_bun)

        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = "sour cream"
        mock_ingredient.get_price.return_value = 100
        self.burger.add_ingredient(mock_ingredient)

        receipt = self.burger.get_receipt()
        
        expected_receipt = "(==== white bun ====)\n= sauce sour cream =\n(==== white bun ====)\n\nPrice: 300"
        assert receipt == expected_receipt

    def test_get_receipt_with_two_ingredients(self):

        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100
        self.burger.set_buns(mock_bun)

        mock_sauce = Mock(spec=Ingredient)
        mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_sauce.get_name.return_value = "hot sauce"
        mock_sauce.get_price.return_value = 100
        self.burger.add_ingredient(mock_sauce)

        mock_filling = Mock(spec=Ingredient)
        mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_filling.get_name.return_value = "cutlet"
        mock_filling.get_price.return_value = 100
        self.burger.add_ingredient(mock_filling)

        receipt = self.burger.get_receipt()
        
        expected_receipt = "(==== black bun ====)\n= sauce hot sauce =\n= filling cutlet =\n(==== black bun ====)\n\nPrice: 400"
        assert receipt == expected_receipt

    def test_get_receipt_complex(self):

        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "test bun"
        mock_bun.get_price.return_value = 150

        mock_sauce = Mock(spec=Ingredient)
        mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_sauce.get_name.return_value = "test sauce"
        mock_sauce.get_price.return_value = 75

        mock_filling = Mock(spec=Ingredient)
        mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_filling.get_name.return_value = "test filling"
        mock_filling.get_price.return_value = 125

        self.burger.set_buns(mock_bun)
        self.burger.add_ingredient(mock_sauce)
        self.burger.add_ingredient(mock_filling)

        receipt = self.burger.get_receipt()
        
        expected_receipt = "(==== test bun ====)\n= sauce test sauce =\n= filling test filling =\n(==== test bun ====)\n\nPrice: 500"
        assert receipt == expected_receipt

    def test_multiple_ingredients_manipulation(self):

        ingredients = []
        for i in range(5):
            mock_ing = Mock(spec=Ingredient)
            mock_ing.get_price.return_value = i * 10
            mock_ing.get_name.return_value = f"ingredient{i}"
            ingredients.append(mock_ing)

        for ing in ingredients:
            self.burger.add_ingredient(ing)

        assert len(self.burger.ingredients) == 5

        self.burger.remove_ingredient(2)
        assert len(self.burger.ingredients) == 4

        self.burger.move_ingredient(3, 0)

        assert len(self.burger.ingredients) == 4