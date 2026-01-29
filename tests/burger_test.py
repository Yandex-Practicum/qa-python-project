from praktikum.burger import Burger
from unittest.mock import Mock
import pytest
import ingredient_types



class TestBurger:

    def test_set_bun_none_true(self, super_burger):
        assert super_burger.bun == None


    def test_set_indridients_empty_true(self, super_burger):
        assert super_burger.ingredients == []


    def test_set_bun_true(self, super_burger):
        mock_bulocka = Mock()
        mock_bulocka.return_value = ingredient_types.BUN_NAME
        super_burger.set_buns(mock_bulocka.return_value)
        assert super_burger.bun == ingredient_types.BUN_NAME


    @pytest.mark.parametrize('ingridient', ingredient_types.INGREDIENT_FOR_BURGERS)
    def test_add_ingredient_one_in_list_true(self, ingridient, super_burger):
        mock_ingridient = Mock()
        mock_ingridient.return_value = ingridient
        super_burger.add_ingredient(mock_ingridient.return_value)
        assert super_burger.ingredients == [ingridient]


    def test_add_ingredient_add_existing_list_true(self, super_burger):
        super_burger.ingredients = ingredient_types.INGREDIENT_FOR_BURGERS
        mock_ingridient = Mock()
        mock_ingridient.return_value = ingredient_types.INGREDIENT_NAME
        super_burger.add_ingredient(mock_ingridient.return_value)
        assert super_burger.ingredients == ingredient_types.INGREDIENT_FOR_BURGERS_PLUS_ONE


    def test_remove_ingredient_from_existing_list_true(self, super_burger):
        super_burger.ingredients = ingredient_types.INGREDIENT_FOR_REMOVE_INGRIDIENTS
        super_burger.remove_ingredient(2)
        assert super_burger.ingredients == ingredient_types.INGREDIENT_FOR_BURGERS_REMOVED


    def test_move_ingredient_from_existing_list_true(self, super_burger):
        super_burger.ingredients = ingredient_types.INGREDIENT_FOR_BURGERS_FOR_MOVE_INGRIDIENTS
        super_burger.move_ingredient(0, 2)
        assert super_burger.ingredients == ingredient_types.INGREDIENT_FOR_BURGERS_MOVED


    def test_get_price_success(self, super_burger, mock_bun, mock_ingredient):
        super_burger.bun = mock_bun
        super_burger.ingredients = [mock_ingredient]
        expected_result = ingredient_types.BUN_PRICE * 2 + ingredient_types.INGREDIENT_PRICE
        assert super_burger.get_price() == expected_result


    def test_get_receipt_success(self, mock_ingredient, mock_bun, mock_burger_price):
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        expected_result = '(==== супер булка ====)\n' \
                          '= супер соус СУПЕР НАПОЛНЕНИЕ =\n' \
                          '(==== супер булка ====)\n' \
                          '\nPrice: 70.0'
        assert burger.get_receipt() == expected_result




