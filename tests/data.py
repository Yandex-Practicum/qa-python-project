import sys
import os
from unittest.mock import Mock

class BunsWithIngred:
    # Моки булок
    mock_buns = []
    mock_bun1 = Mock()
    mock_bun1.get_name.return_value = "white bun"
    mock_bun1.get_price.return_value = 200.0
    mock_bun2 = Mock()
    mock_bun2.get_name.return_value = "red bun"
    mock_bun2.get_price.return_value = 300.0
    mock_buns.append(mock_bun1)
    mock_buns.append(mock_bun2)

    # Моки ингредиентов
    mock_ingredients = []
    mock_ingredient1 = Mock()
    mock_ingredient1.get_name.return_value = "chili sauce"
    mock_ingredient1.get_price.return_value = 300.0
    mock_ingredient1.get_type.return_value = 'SAUCE'
    mock_ingredient2 = Mock()
    mock_ingredient2.get_name.return_value = "cutlet"
    mock_ingredient2.get_price.return_value = 100.0
    mock_ingredient2.get_type.return_value = 'FILLING'
    mock_ingredients.append(mock_ingredient1)
    mock_ingredients.append(mock_ingredient2)

    @staticmethod
    def get_my_receipt(bun, ingredients):
        # Если передан не список (а одиночный объект), оборачиваем его в список
        if not isinstance(ingredients, list):
            ingredients = [ingredients]

        my_receipt = ""
        total_price = 0

        if bun is not None:
            my_receipt += f'(==== {bun.get_name()} ====)\n'
            total_price += bun.get_price() * 2

        for ingredient in ingredients:
            my_receipt += f'= {str(ingredient.get_type()).lower()} {ingredient.get_name()} =\n'
            total_price += ingredient.get_price()

        if bun is not None:
            my_receipt += f'(==== {bun.get_name()} ====)\n\n'
        else:
            my_receipt += "\n"

        my_receipt += f'Price: {total_price}'
        return my_receipt
