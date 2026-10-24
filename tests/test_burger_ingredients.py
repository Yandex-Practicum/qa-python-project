from praktikum.burger import Burger
from praktikum.bun import Bun
import pytest
from praktikum.ingredient import Ingredient
from unittest.mock import Mock


@pytest.mark.parametrize(
    'ingredient_type, name, price',
    [
        ('FILLING', 'cutlet', 200),
        ('SAUCE', 'hot sauce', 100),
    ]
)
def test_add_ingredient(ingredient_type, name, price):

    burger = Burger()
    ingredient = Ingredient(ingredient_type, name, price)
    burger.add_ingredient(ingredient)
    
    assert burger.ingredients == [ingredient]



def test_remove_ingredient(create_ingredient_cutlet, create_ingredient_sauce):

    burger = Burger()

    burger.add_ingredient(create_ingredient_cutlet)
    burger.add_ingredient(create_ingredient_sauce)
    
    burger.remove_ingredient(0)

    assert burger.ingredients == [create_ingredient_sauce]



def test_move_ingredient(create_ingredient_cutlet, create_ingredient_sauce):
    
    burger = Burger()

    burger.add_ingredient(create_ingredient_cutlet)
    burger.add_ingredient(create_ingredient_sauce)

    burger.move_ingredient(0, 1)

    assert burger.ingredients == [create_ingredient_sauce, create_ingredient_cutlet]
