from burger import Burger
from unittest.mock import Mock


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

    def test_move_ingredient(self):
        mock_1 = Mock()
        mock_2 = Mock()
        burger = Burger()
        burger.add_ingredient(mock_1)
        burger.add_ingredient(mock_2)
        burger.move_ingredient(0,1)
        assert burger.ingredients[0] == mock_2

    def test_get_price(self):
        mock_bun = Mock()
        mock_ingredient = Mock()
        mock_bun.get_price.return_value = 100
        mock_ingredient.get_price.return_value = 50
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 250

    def test_get_receipt(self):
        mock_bun = Mock()
        mock_ingredient = Mock()
        mock_bun.get_price.return_value = 100
        mock_bun.get_name.return_value = "Метеоритная булка"
        mock_ingredient.get_name.return_value = "Лунный Тар-Тар"
        mock_ingredient.get_price.return_value = 50
        mock_ingredient.get_type.return_value = "SAUCE"
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
        assert "Метеоритная булка" in receipt
        assert "sauce" in receipt
        assert "Лунный Тар-Тар" in receipt
        assert "250" in receipt
