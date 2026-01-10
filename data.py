# Data for tests
from praktikum.ingredient_types import *

BUN = {'name': 'FLOAT Buuuuulka', 'price': 118.5}
BUN2 = {'name': 'INTEGER Price Bun', 'price': 111}
INGREDIENT = {'ingredient_type': INGREDIENT_TYPE_SAUCE, 'name': 'INTEGER Tester\'s tears', 'price': 999}
INGREDIENT2 = {'ingredient_type': INGREDIENT_TYPE_FILLING, 'name': 'FLOAT customer\'s expectations', 'price': 258.6}

TMPL_BUN = '(==== {bun_name} ====)'
TMPL_INGR = '= {ingredient_type} {ingredient_name} ='
TMPL_PRICE = '\nPrice: {price}'
RECEIPT_TEMPLATE = '\n'.join([TMPL_BUN, TMPL_INGR, TMPL_BUN, TMPL_PRICE])

BUNS_DATA = [('black bun', 100), ('white bun', 200), ('red bun', 300)]
INGR_DATA = [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
    (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
    (INGREDIENT_TYPE_FILLING, "cutlet", 100),
    (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    (INGREDIENT_TYPE_FILLING, "sausage", 300)
]
