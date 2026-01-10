import random
from unittest.mock import Mock

PRICES = [100, 200, 300]
BUNS_NAMES = ["black bun", "white bun", "red bun"]
SAUCES_NAMES = ["hot sauce", "sour cream", "chili sauce"]
FILLINGS_NAMES = ["cutlet", "dinosaur", "sausage"]

def get_random_value(arr):
    return random.choice(arr)

def make_mock(name, price, ingredient_type=None):
    mock = Mock()
    mock.get_name.return_value = name
    mock.get_price.return_value = price
    if ingredient_type is not None:
        mock.get_type.return_value = ingredient_type
    return mock

def buns_generator():
    result = []
    for i in range(3):
        bun = make_mock(BUNS_NAMES[i], PRICES[i])
        result.append(bun)
    return result

def ingredients_generator(ingredient_type):
    result = []
    for i in range(3):
        name = SAUCES_NAMES[i] if ingredient_type == 'SAUCE' else FILLINGS_NAMES[i]
        ingredient = make_mock(name, PRICES[i], ingredient_type)
        result.append(ingredient)
    return result
