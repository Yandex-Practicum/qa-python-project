from unittest.mock import Mock, patch
from data import BUN_NAME, BUN_PRICE, BURGER_FULL_RECEIPT, BURGER_PRICE, INGREDIENT_NAME, INGREDIENT_PRICE
from practicum.ingredient import Ingredient
from practicum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestBurger:

    def test_set_buns(self, burger_empty, bun_fixture):        
        burger_empty.set_buns(bun_fixture)
        assert burger_empty.bun.name == BUN_NAME and burger_empty.bun.price == BUN_PRICE

    def test_add_ingredient(self, burger_empty, ingredient_fixture):        
        burger_empty.add_ingredient(ingredient_fixture)
        assert (burger_empty.ingredients[0].name == INGREDIENT_NAME 
                and burger_empty.ingredients[0].type == INGREDIENT_TYPE_SAUCE 
                and burger_empty.ingredients[0].price == INGREDIENT_PRICE)
            
    def test_remove_ingredient(self, burger_empty, ingredient_fixture):
        burger_empty.ingredients = [ingredient_fixture]
        burger_empty.remove_ingredient(0)
        assert burger_empty.ingredients == []

    def test_move_ingredient(self, burger_empty, ingredient_fixture):
        ingredient_1  = ingredient_fixture
        ingredient_2  = Mock(spec=Ingredient)
        burger_empty.ingredients = [ingredient_1 , ingredient_2]
        burger_empty.move_ingredient(1, 0)
        assert burger_empty.ingredients == [ingredient_2 , ingredient_1]

    def test_get_price(self, burger_full):
        burger_price = burger_full.get_price()
        assert burger_price == BURGER_PRICE

    @patch('practicum.burger.Burger.get_price', return_value=BURGER_PRICE)
    def test_get_receipt(self, mock_burger_get_price, burger_full):
        burger_receipt = burger_full.get_receipt()
        assert burger_receipt == BURGER_FULL_RECEIPT