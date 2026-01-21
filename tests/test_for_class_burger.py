import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from data_for_tests.data_for_buns import DataBuns
from data_for_tests.data_ingrid import DataIngrid
from data_for_tests.data_expected_receipt import ExpectedReceipt
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:
   
    @pytest.mark.parametrize("name, price", DataBuns.buns)
    def test_burg_set_buns(self, name, price):
        burger = Burger()
        bun = Bun(name, price)
        burger.set_buns(bun)
        assert burger.bun == bun

   
    @pytest.mark.parametrize("ingredient_type, name, price", DataIngrid.all_ingrids)
    def test_burg_add_ingredient(self, ingredient_type, name, price):
        burger = Burger()
        ingrid = Ingredient(ingredient_type, name, price)
        burger.add_ingredient(ingrid)
        assert ingrid in burger.ingredients

    @pytest.mark.parametrize("ingredient_type, name, price", DataIngrid.all_ingrids)
    def test_burg_remove_ingredient(self, ingredient_type, name, price):
        burger = Burger()
        ingrid1 = Ingredient(ingredient_type, name, price)
        burger.add_ingredient(ingrid1)
        ingrid2 = Ingredient(ingredient_type, name, price)
        burger.add_ingredient(ingrid2)
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 1

  
    @pytest.mark.parametrize("ingredient_type, name, price", DataIngrid.all_ingrids)
    def test_burg_move_ingredient(self, ingredient_type, name, price):
        burger = Burger()
        ingrid1 = Ingredient(ingredient_type, name, price)
        burger.add_ingredient(ingrid1)
        ingrid2 = Ingredient(ingredient_type, name, price)
        burger.add_ingredient(ingrid2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingrid2
        assert burger.ingredients[1] == ingrid1

 
    @pytest.mark.parametrize("name_b, price_b", DataBuns.buns)
    @pytest.mark.parametrize("ingredient_type, name, price", DataIngrid.all_ingrids)
    def test_burg_get_price(self, name_b, price_b, ingredient_type, name, price):
        burger = Burger()
        bun = Bun(name_b, price_b)
        burger.set_buns(bun)
        bun_price = burger.bun.get_price() * 2        
        ingrid = Ingredient(ingredient_type, name, price)
        burger.add_ingredient(ingrid)        
        ingr_price = ingrid.get_price()
        fin_price = bun_price + ingr_price
        assert burger.get_price() == fin_price


    def test_burg_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()

        mock_bun.get_name.return_value = DataBuns.buns[0][0]
        mock_bun.get_price.return_value = DataBuns.buns[0][1]
        burger.bun = mock_bun

        mock_ingr1 = Mock()
        mock_ingr1.get_name.return_value = DataIngrid.all_ingrids[11][1]
        mock_ingr1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingr1.get_price.return_value = DataIngrid.all_ingrids[11][2]

        mock_ingr2 = Mock()
        mock_ingr2.get_name.return_value = DataIngrid.all_ingrids[5][1]
        mock_ingr2.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingr2.get_price.return_value = DataIngrid.all_ingrids[5][2]

        mock_ingr3 = Mock()
        mock_ingr3.get_name.return_value = DataIngrid.all_ingrids[7][1]
        mock_ingr3.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingr3.get_price.return_value = DataIngrid.all_ingrids[7][2]

        burger.ingredients = [mock_ingr1, mock_ingr2, mock_ingr3]

        assert  burger.get_receipt() == ExpectedReceipt.expected_receipt