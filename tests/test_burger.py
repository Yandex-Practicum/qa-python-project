import pytest
from unittest.mock import Mock
 
from burger import Burger

class TestBurger:
 
    def test_set_buns_sets_bun(self):
        burger = Burger()
 
        bun = Mock()
        bun.get_name.return_value = "булка"
        bun.get_price.return_value = 100
 
        burger.set_buns(bun)
 
        assert burger.bun == bun
 
    def test_add_ingredient_adds_ingredient(self):
        burger = Burger()
 
        ingredient = Mock()
        ingredient.get_type.return_value = "соус"
        ingredient.get_name.return_value = "кетчуп"
        ingredient.get_price.return_value = 50
 
        burger.add_ingredient(ingredient)
 
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient
 
    def test_remove_ingredient_removes_ingredient(self):
        burger = Burger()
 
        ingredient_1 = Mock()
        ingredient_1.get_name.return_value = "кетчуп"
 
        ingredient_2 = Mock()
        ingredient_2.get_name.return_value = "котлетв"
 
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
 
        burger.remove_ingredient(0)
 
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_2
 
    def test_move_ingredient_moves_ingredient(self):
        burger = Burger()
 
        ingredient_1 = Mock()
        ingredient_1.get_name.return_value = "кетчуп"
 
        ingredient_2 = Mock()
        ingredient_2.get_name.return_value = "котлета"
 
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
 
        burger.move_ingredient(0, 1)
 
        assert burger.ingredients[0] == ingredient_2
        assert burger.ingredients[1] == ingredient_1
 
    @pytest.mark.parametrize(
        "bun_price, ingredient_price, expected_price",
        [
            (100, 50, 250),
            (200, 100, 500),
        ]
    )
    def test_get_price_returns_correct_price(self, bun_price, ingredient_price, expected_price):
        burger = Burger()
 
        bun = Mock()
        bun.get_name.return_value = "булочка"
        bun.get_price.return_value = bun_price
 
        ingredient = Mock()
        ingredient.get_type.return_value = "соус"
        ingredient.get_name.return_value = "кетчуп"
        ingredient.get_price.return_value = ingredient_price
 
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
 
        assert burger.get_price() == expected_price
 
    def test_get_receipt_returns_correct_receipt(self):
        burger = Burger()
 
        bun = Mock()
        bun.get_name.return_value = "булочка"
        bun.get_price.return_value = 100
 
        ingredient = Mock()
        ingredient.get_type.return_value = "соус"
        ingredient.get_name.return_value = "кетчуп"
        ingredient.get_price.return_value = 50
 
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
 
        expected_receipt = (
            "(==== булочка ====)\n"
            "= соус кетчуп =\n"
            "(==== булочка ====)\n\n"
            "Price: 250"
        )
 
        assert burger.get_receipt() == expected_receipt