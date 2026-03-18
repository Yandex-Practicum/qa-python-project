from praktikum.burger import Burger
from unittest.mock import Mock
from praktikum.ingredient_types import *
import pytest

class TestBurger:
    
    
    @pytest.mark.parametrize('bun_name', [
        'Флюоресцентная булка R2-D3',
        'Краторная булка N-200i'
    ])
    def test_buns(self, bun_name):
        bun = Mock()
        bun.name = bun_name
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun.name == bun_name   

    @pytest.mark.parametrize('ingredient_name', [
        'Мясо бессмертных моллюсков Protostomia'        
    ])
    def test_ingredient(self, ingredient_name):
        ingredient = Mock()
        ingredient.name = ingredient_name
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert burger.ingredients[0].name == ingredient_name

   
    @pytest.mark.parametrize('ingredient_name', [
        'Соус Spicy-X',
        'Соус фирменный Space Sauce',
        'Соус традиционный галактический',
        'Соус с шипами Антарианского плоскоходца'
    ]) 
    def test_remove_ingredient(self, ingredient_name):
        ingredient = Mock()
        ingredient.name = ingredient_name
        burger = Burger()
        burger.add_ingredient(ingredient)
        len(burger.ingredients) == 1
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    @pytest.mark.parametrize('ingredient1_name, ingredient2_name', [
        ('Соус Spicy-X', 'Мясо бессмертных моллюсков Protostomia')
        
    ]) 
    def test_move_ingredient(self, ingredient1_name, ingredient2_name):
        ingredient1 = Mock()
        ingredient1.name = ingredient1_name
        ingredient2 = Mock()
        ingredient2.name = ingredient2_name
        burger = Burger()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.ingredients[0].name == ingredient1_name
        burger.ingredients[1].name == ingredient2_name
        burger.move_ingredient(1, 0)
        burger.ingredients[0].name == ingredient2_name
        assert burger.ingredients[1].name == ingredient1_name

    @pytest.mark.parametrize('bun_price, ingredient_price, ingredient2_price, expected_price', [
        (988, 80, 1337, 3393),
        (1255, 90, 3000, 5600)
    ])
    def test_get_price(self, bun_price, ingredient_price, ingredient2_price, expected_price):
        bun = Mock()
        bun.get_price.return_value = bun_price

        ingredient = Mock()
        ingredient.get_price.return_value = ingredient_price

        ingredient2 = Mock()
        ingredient2.get_price.return_value = ingredient2_price

        burger = Burger()
        burger.set_buns(bun)       
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient2)

        price = burger.get_price()
        assert price == expected_price

    @pytest.mark.parametrize('bun_name, bun_price, ingredient_name, ingredient_type, ingredient_price, ingredient2_name, ingredient2_type, ingredient2_price, expected_receipt', [
        (
            'Флюоресцентная булка R2-D3', 988,
            'Соус фирменный Space Sauce', INGREDIENT_TYPE_SAUCE, 80,
            'Мясо бессмертных моллюсков Protostomia', INGREDIENT_TYPE_FILLING, 1337,
            '(==== Флюоресцентная булка R2-D3 ====)\n= sauce Соус фирменный Space Sauce =\n= filling Мясо бессмертных моллюсков Protostomia =\n(==== Флюоресцентная булка R2-D3 ====)\n\nPrice: 3393'
        ),
        (
            'Краторная булка N-200i', 1255,
            'Соус Spicy-X', INGREDIENT_TYPE_SAUCE, 90,
            'Говяжий метеорит (отбивная)', INGREDIENT_TYPE_FILLING, 3000,
            '(==== Краторная булка N-200i ====)\n= sauce Соус Spicy-X =\n= filling Говяжий метеорит (отбивная) =\n(==== Краторная булка N-200i ====)\n\nPrice: 5600'
        )
    ])
    def test_get_receipt(self, bun_name, bun_price, ingredient_name, ingredient_type, ingredient_price, ingredient2_name, ingredient2_type, ingredient2_price, expected_receipt):
        bun = Mock()
        bun.get_name.return_value = bun_name
        bun.get_price.return_value = bun_price

        ingredient = Mock()
        ingredient.get_name.return_value = ingredient_name
        ingredient.get_type.return_value = ingredient_type
        ingredient.get_price.return_value = ingredient_price

        ingredient2 = Mock()
        ingredient2.get_name.return_value = ingredient2_name
        ingredient2.get_type.return_value = ingredient2_type
        ingredient2.get_price.return_value = ingredient2_price

        burger = Burger()
        burger.set_buns(bun)       
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient2)

        receipt = burger.get_receipt()
        assert receipt == expected_receipt       