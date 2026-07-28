import pytest
from unittest.mock import Mock
from burger import Burger

class TestBurger:

    def test_set_buns (self): 
        mock_bun = Mock()
        burger = Burger()
        burger.set_buns(mock_bun)
        
        assert burger.bun == mock_bun

    
    def test_add_ingredient (self):
        mock_ingredient = Mock()
        burger=Burger()
        burger.add_ingredient(mock_ingredient)
        
        assert burger.ingredients[0] == mock_ingredient
        assert len(burger.ingredients) == 1 
        
    
    def test_remove_ingredient_delete_ingredient (self):
        mock_ingredient =Mock()
        burger = Burger()

        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0] == mock_ingredient
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == 0
    

    @pytest.mark.parametrize(
        'index, new_index, names',
        [
            [0,1, ['Сыр','Мини-салат','Филе']],
            [1,2, ['Мини-салат','Филе','Сыр']],
            [2,0, ['Филе','Мини-салат','Сыр']]
        ]
    )
    def test_move_ingredient (self,index, new_index, names):
        
        mock_salad = Mock()
        mock_salad.get_name.return_value = 'Мини-салат'

        mock_cheese = Mock()
        mock_cheese.get_name.return_value = 'Сыр'

        mock_fillet = Mock()
        mock_fillet.get_name.return_value = 'Филе'

        burger=Burger()
        
        burger.add_ingredient(mock_salad)
        burger.add_ingredient(mock_cheese)
        burger.add_ingredient(mock_fillet)

        burger.move_ingredient(index, new_index)

        actual_names = []

        for i in burger.ingredients:
            name = i.get_name()
            actual_names.append(name)

        assert actual_names == names
        
    def test_get_price (self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 1255

        mock_fillet = Mock()
        mock_fillet.get_price.return_value = 988

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_fillet)

        assert burger.get_price() == 3498

    def test_get_receipt (self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 1255
        mock_bun.get_name.return_value = 'Краторная булка N-200i'

        mock_sauce = Mock()
        mock_sauce.get_price.return_value = 90
        mock_sauce.get_type.return_value = 'SAUCE'
        mock_sauce.get_name.return_value = 'Соус Spicy-X'

        mock_fillet = Mock()
        mock_fillet.get_price.return_value = 988
        mock_fillet.get_type.return_value = 'FILLING'
        mock_fillet.get_name.return_value = 'Филе Люминесцентного тетраодонтимформа'

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_fillet)

        assert 'Price: 3588' in burger.get_receipt()
        assert 'Краторная булка N-200i' in burger.get_receipt()
        assert 'sauce Соус Spicy-X' in burger.get_receipt()
        assert 'filling Филе Люминесцентного тетраодонтимформа' in burger.get_receipt()
