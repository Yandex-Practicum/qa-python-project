from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
import pytest
class TestBurger:
    def test_set_buns(self, mock_bun, burger):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun
            
    @pytest.mark.parametrize("ingredient", [(INGREDIENT_TYPE_FILLING, "TestFilling", 1.0), (INGREDIENT_TYPE_SAUCE, "TestSauce", 1.0)])
    def test_add_ingredient(self, ingredient, burger):
        test_ingredient = Ingredient(*ingredient)
        burger.add_ingredient(test_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients == [test_ingredient]

    def test_remove_ingredient(self, burger, mock_filling, mock_sauce):
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_sauce)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients == [mock_sauce]

    def test_move_ingredient(self, burger, mock_filling, mock_sauce):
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_sauce)
        burger.move_ingredient(0,1)
        assert burger.ingredients == [mock_sauce, mock_filling]


    @pytest.mark.parametrize("ingredient, target_price", [((INGREDIENT_TYPE_FILLING, "TestFilling", 1.0), 3.0), 
                                            ((INGREDIENT_TYPE_SAUCE, "TestSauce", 2.0), 4.0)])
    def test_get_price(self, burger, mock_bun, ingredient, target_price):
        burger.set_buns(mock_bun)        
        burger.add_ingredient(Ingredient(*ingredient))
        assert burger.get_price() == target_price

    @pytest.mark.parametrize("ingredient, receipt", [((INGREDIENT_TYPE_FILLING, "TestFilling", 1.0), 
'''(==== TestBun2000 ====)
= filling TestFilling =
(==== TestBun2000 ====)

Price: 3.0'''), 
                                            ((INGREDIENT_TYPE_SAUCE, "TestSauce", 2.0), 
'''(==== TestBun2000 ====)
= sauce TestSauce =
(==== TestBun2000 ====)

Price: 4.0''')])
    def test_get_receipt(self, burger, mock_bun, ingredient, receipt):
        burger.set_buns(mock_bun)        
        burger.add_ingredient(Ingredient(*ingredient))
        assert burger.get_receipt() == receipt