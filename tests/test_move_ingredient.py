from unittest.mock import Mock 
import pytest
from praktikum.burger import Burger


class TestRemoveIngredient:

    '''
    Проверяется метод  перемещения ингредиентов
    def move_ingredient(self, index: int, new_index: int):
        self.ingredients.insert(new_index, self.ingredients.pop(index))
    ''' 

    @pytest.mark.parametrize("move_from, move_to, expected_burger", [
    (0, 2, ["dinosaur", "cutlet", "sour cream"]),  # первый в конец
    (2, 0, ["cutlet", "sour cream", "dinosaur"]),  # последний в начало
    (1, 2, ["sour cream", "cutlet", "dinosaur"]),  # средний в конец
    (1, 0, ["dinosaur", "sour cream", "cutlet"]),  # средний в начало
    ])
    def test_move_ingredient_param(self, move_from, move_to, expected_burger):
        burger = Burger()
    
        ingredients = [
            Mock(get_name=Mock(return_value="sour cream")),
            Mock(get_name=Mock(return_value="dinosaur")),
            Mock(get_name=Mock(return_value="cutlet"))
        ]
    
        for ing in ingredients:
            burger.add_ingredient(ing)
    
        burger.move_ingredient(move_from, move_to)

        result_names = []                    
        for ing in burger.ingredients:
            name = ing.get_name()
            result_names.append(name)

        assert result_names == expected_burger, \
            f"Ожидался порядок {expected_burger}, получен {result_names}"
        