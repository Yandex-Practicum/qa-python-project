from unittest.mock import Mock
from praktikum.burger import Burger

class TestBurger:
    
    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    
    def test_add_ingridient(self):
        burger = Burger()
        mock_ingridient = Mock()
        burger.add_ingredient(mock_ingridient)

        assert mock_ingridient in burger.ingredients


    def test_remove_ingridient(self):
        burger = Burger()
        mock_ingridient = Mock()
        burger.ingredients = [mock_ingridient]
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0


    def test_move_ingridients(self):
        burger = Burger()
        mock_ingridient_1 = Mock()
        mock_ingridient_2 = Mock()
        burger.add_ingredient(mock_ingridient_1)
        burger.add_ingredient(mock_ingridient_2)

        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ingridient_2, mock_ingridient_1]


    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 1000
        burger.set_buns(mock_bun)
        mock_ingridient = Mock()
        mock_ingridient.get_price.return_value = 500
        burger.ingredients = [mock_ingridient]

        assert burger.get_price() == 2500

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Краторная булка N-200i"
        mock_bun.get_price.return_value = 1255
        burger.set_buns(mock_bun)

        mock_ingridient = Mock()
        mock_ingridient.get_type.return_value = "SAUCE"
        mock_ingridient.get_name.return_value = "Соус традиционный галактический"
        mock_ingridient.get_price.return_value = 15
        burger.ingredients = [mock_ingridient]
        receipt = burger.get_receipt()

        assert "==== Краторная булка N-200i ====" in receipt
        assert "sauce Соус традиционный галактический" in receipt
        assert "Price: 2525" in receipt