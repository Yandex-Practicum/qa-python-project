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
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        mock_ing1 = Mock()
        mock_ing2 = Mock()
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ing2
        assert burger.ingredients[1] == mock_ing1

    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        mock_ing = Mock()
        mock_ing.get_price.return_value = 50
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing)
        assert burger.get_price() == 250

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Булка"
        mock_bun.get_price.return_value = 100
        
        mock_ing = Mock()
        mock_ing.get_type.return_value = "FILLING"
        mock_ing.get_name.return_value = "Мясо"
        mock_ing.get_price.return_value = 50

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing)

        receipt = burger.get_receipt()
        assert "(==== Булка ====)" in receipt
        assert "= filling Мясо =" in receipt
        assert "Price: 250" in receipt