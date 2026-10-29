import pytest
import pytest_cov
from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:
   
   def test_set_buns(self):
      burger = Burger()
      mock_bun = Mock()
      burger.set_buns(mock_bun)

      assert burger.bun == mock_bun
     

   def test_add_ingredient(self):
      burger = Burger()
      mock_ingredient = Mock()
      burger.add_ingredient(mock_ingredient)

      assert mock_ingredient in burger.ingredients


   def test_remove_ingredient(self):
      burger = Burger()
      mock_ingredient = Mock()
      burger.add_ingredient(mock_ingredient)
      burger.remove_ingredient(0)

      assert mock_ingredient not in burger.ingredients
      assert len(burger.ingredients) == 0


   @pytest.mark.parametrize(
         "index, new_index, list_ingredients",
      [
         (1, 2, [0, 2, 1]),
         (2, 0, [1, 2, 0]),
         (0, 1, [1, 0, 2]),
      ]
   )
   def test_move_ingredient(self, index, new_index, list_ingredients):
      burger = Burger()

      mock_ingredient_1 = Mock()
      mock_ingredient_2 = Mock()
      mock_ingredient_3 = Mock()
      
      burger.add_ingredient(mock_ingredient_1)
      burger.add_ingredient(mock_ingredient_2)
      burger.add_ingredient(mock_ingredient_3)

      burger.move_ingredient(index, new_index)

      indexes_ingredients = [
         burger.ingredients.index(mock_ingredient_1),
         burger.ingredients.index(mock_ingredient_2),
         burger.ingredients.index(mock_ingredient_3)
      ]

      assert indexes_ingredients == list_ingredients


   @pytest.mark.parametrize( 
   "bun_price, ingredients_prices, total_price",
   [
      (100, [], 200),
      (200, [100, 50], 550),
      (300, [200], 800),
   ]
)
   def test_get_price(self, bun_price, ingredients_prices, total_price):
      burger = Burger()

      mock_bun = Mock()
      mock_bun.get_price.return_value = bun_price
      burger.set_buns(mock_bun)

      for price in ingredients_prices:
         mock_ingredient = Mock()
         mock_ingredient.get_price.return_value = price
         burger.add_ingredient(mock_ingredient) 
      
      assert burger.get_price() == total_price


   @pytest.mark.parametrize( 
      "bun_name, bun_price, ingredients_name, ingredients_type, ingredients_prices, total_price",
      [
         ("black bun", 100, ["chili sauce"], ['SAUCE'], [200], 400),
         ("white bun", 200, ["dinosaur", "hot sauce"], ['FILLING', 'SAUCE'], [100, 200], 700),
         ("red bun", 300, ["sausage"], ['FILLING'], [300], 900),
      ]
   )
   def test_get_receipt(self, bun_name, bun_price, ingredients_name, ingredients_type, ingredients_prices, total_price):
      burger = Burger()
      
      mock_bun = Mock()
      mock_bun.get_name.return_value = bun_name
      mock_bun.get_price.return_value = bun_price
      burger.set_buns(mock_bun)   
      
      for name, ingredient_type, price in zip(ingredients_name, ingredients_type, ingredients_prices):
         mock_ingredient = Mock()
         mock_ingredient.get_name.return_value = name
         mock_ingredient.get_type.return_value = ingredient_type
         mock_ingredient.get_price.return_value = price

         burger.add_ingredient(mock_ingredient)
      
      receipt = burger.get_receipt()

      assert bun_name in receipt
      assert str(total_price) in receipt

      for name in ingredients_name:
         assert name in receipt