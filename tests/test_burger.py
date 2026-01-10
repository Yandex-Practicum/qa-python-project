from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:
    def test_set_buns_one_bun(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Краторная булка N-200i'
        mock_bun.get_price.return_value = 1255
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_from_ingredients_list(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = 'FILLING'
        mock_ingredient.get_name.return_value = 'Сыр с астероидной плесенью'
        mock_ingredient.get_price.return_value = 100
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient_list_is_empty(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.ingredients = [mock_ingredient]
        burger.remove_ingredient(0)
        assert not burger.ingredients

    def test_move_ingredient_successful_move(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [mock_ingredient_2, mock_ingredient_1]

    def test_get_price_correct(self):
        burger = Burger()
        mock_bun = Mock()
        mock_ingredient = Mock()
        mock_bun.get_price.return_value = 100
        mock_ingredient.get_price.return_value = 10
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        assert burger.get_price() == 210

    def test_get_receipt_correct(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Краторная булка N-200i'
        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_type.return_value = 'SAUCE'
        mock_ingredient_1.get_name.return_value = 'Соус с шипами Антарианского плоскоходца'
        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_type.return_value = 'FILLING'
        mock_ingredient_2.get_name.return_value = 'Сыр с астероидной плесенью'
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]
        burger.get_price = Mock(return_value=1000)

        receipt = ("(==== Краторная булка N-200i ====)\n= sauce Соус с шипами Антарианского плоскоходца =\n= "
                   "filling Сыр с астероидной плесенью =\n(==== Краторная булка N-200i ====)\n\nPrice: 1000")
        assert burger.get_receipt() == receipt
