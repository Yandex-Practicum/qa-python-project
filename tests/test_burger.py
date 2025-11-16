from unittest.mock import Mock
import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestBurger:


    @pytest.mark.parametrize('bun_name,price',[
        ('Флюоресцентная булка', 100),
        ('Краторная булка', 200)
    ])
    def test_set_buns_success(self, burger, bun_name, price):
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = price
        burger.set_buns(mock_bun)
        assert burger.bun.get_name() == bun_name and burger.bun.get_price() == price


    def test_add_igredient_success(self, burger):
        mock_igredient = Mock()
        mock_igredient.get_name.return_value = 'Соус Spicy-X'
        mock_igredient.get_type.return_value = 'Соус'
        mock_igredient.get_price.return_value = 90
        burger.add_ingredient(mock_igredient)
        assert len(burger.ingredients) == 1 and burger.ingredients[0].get_type() == 'Соус'


    def test_remove_igredient_success(self, burger):
        mock_igredient = Mock()
        burger.add_ingredient(mock_igredient)
        burger.add_ingredient(mock_igredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1


    @pytest.mark.parametrize('name_1,name_2', [
        ('hot sauce', 'sour cream'),
        ('cutlet', 'sausage')
    ])
    def test_move_igredient_success(self, burger, name_1, name_2):
        mock_igredient_1 = Mock()
        mock_igredient_1.get_name.return_value = name_1
        mock_igredient_2 = Mock()
        mock_igredient_2.get_name.return_value = name_2
        burger.add_ingredient(mock_igredient_1)
        burger.add_ingredient(mock_igredient_2)
        burger.move_ingredient(0,1)
        assert burger.ingredients[1].get_name() == name_1


    def test_get_price_with_only_bun_success(self, burger, mock_bun):
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        assert burger.get_price() == 200


    def test_get_price_for_buns_and_ingredients_both_success(self, burger, mock_bun, mock_ingredient):
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        mock_ingredient.get_price.return_value = 100
        burger.add_ingredient(mock_ingredient)
        expected_price = 100 * 2 + 100
        assert burger.get_price() == expected_price


    @pytest.mark.parametrize('name_bun,name_ingredient,type_ingredient,bun_price',[
        ('black bun', 'hot sauce', INGREDIENT_TYPE_SAUCE, 50),
        ('white bun', 'sour cream', INGREDIENT_TYPE_SAUCE, 100)
    ])
    def test_get_receipt_success(self, burger, mock_bun, mock_ingredient, name_bun,name_ingredient,type_ingredient, bun_price):
        mock_bun.get_price.return_value = bun_price
        mock_bun.get_name.return_value = name_bun
        burger.set_buns(mock_bun)
        mock_ingredient.get_price.return_value = 100
        mock_ingredient.get_type.return_value = type_ingredient
        mock_ingredient.get_name.return_value =  name_ingredient
        burger.add_ingredient(mock_ingredient)
        assert (name_bun, type_ingredient, name_ingredient) and f'Price: {burger.get_price()}' in burger.get_receipt().split('\n')
