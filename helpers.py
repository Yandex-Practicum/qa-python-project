import random
import string
from unittest.mock import Mock

from praktikum.ingredient import Ingredient
import praktikum.ingredient_types as it


class GenerateData:

    @classmethod
    def generate_string(cls, length):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(length))
    

    @classmethod
    def generate_num(cls, min=1, max=100):
        return random.randint(min, max)
    


class CreateObject:

    @classmethod
    def create_mock_ingredient (cls):
        mock_ingr = Mock()
        mock_ingr.type = mock_ingr.get_type.return_value = random.choice([it.INGREDIENT_TYPE_FILLING, it.INGREDIENT_TYPE_SAUCE])
        mock_ingr.name = mock_ingr.get_name.return_value = 'ingr_' + GenerateData.generate_string(4)
        mock_ingr.price = mock_ingr.get_price.return_value = 100 + GenerateData.generate_num(1,90)
        return mock_ingr
    

    @classmethod
    def create_list_mock_ingredients (cls, quantity):
        list_mock_ingr = []
        for i in range(quantity):
            list_mock_ingr.append(cls.create_mock_ingredient())
        return list_mock_ingr
    

    @classmethod
    def calculate_price_list_ingredients(cls, list_ingr):
        length = len(list_ingr)
        sum = 0
        for i in range (length):
            sum += list_ingr[i].price
        return sum

    @classmethod
    def create_mock_bun (cls):
        mock_bun = Mock()
        mock_bun.name = mock_bun.get_name.return_value = 'bulka_' + GenerateData.generate_string(4)
        mock_bun.price = mock_bun.get_price.return_value = 200 + GenerateData.generate_num(1,90)
        return mock_bun
    
