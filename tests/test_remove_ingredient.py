from unittest.mock import Mock 
import pytest
from praktikum.burger import Burger

class TestRemoveIngdient:
    
    
    '''
    Проверяется метод  удаления ингредиентов
    def remove_ingredient(self, index: int):
        del self.ingredients[index]
    ''' 

    def test_remove_ingredient(self):
        burger = Burger()
   
        ingredients = [
            Mock(get_name=Mock(return_value="sour cream")),
            Mock(get_name=Mock(return_value="dinosaur")),
            Mock(get_name=Mock(return_value="cutlet"))
        ]

        for ing in ingredients:
            burger.add_ingredient(ing)
  
        burger.remove_ingredient(1)
            
        assert len(burger.ingredients) == 2, \
            f"ожидалось 2 ингредиента, получено {len(burger.ingredients)}"
        assert burger.ingredients[0] is ingredients[0], \
            f"ожидалось  sour cream"
        assert burger.ingredients[1] is ingredients[2] , \
            f"ожидалось cutlet"
        
    #Проверяем ошибку при несуществующем индексе
    def test_remove_ingredient_invalid_index(self):
        burger = Burger()
        burger.add_ingredient(Mock())  # один ингредиент
    
        with pytest.raises(IndexError):
            burger.remove_ingredient(5)  # ожидается ошибка по индексу

    #Проверяем ошибку при пустом бургере, без ингредиентов
    def test_remove_from_empty_burger(self):
        burger = Burger() 
    
        with pytest.raises(IndexError):
            burger.remove_ingredient(0) # ожидается ошибка по индексу
