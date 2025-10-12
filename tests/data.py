import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


# Данные для моков
BUN_NAME = "Белая булочка"
BUN_PRICE = 100

INGREDIENT_NAME = "Соус острый"
INGREDIENT_TYPE = INGREDIENT_TYPE_SAUCE
INGREDIENT_PRICE = 50

FILLING_NAME = "Котлета"
FILLING_TYPE = INGREDIENT_TYPE_FILLING
FILLING_PRICE = 200

# Данные для параметризованных тестов цены
PRICE_TEST_DATA = [
    ("Белая булочка", "Соус острый", INGREDIENT_TYPE_SAUCE, 250),
    ("Черная булочка", "Котлета", INGREDIENT_TYPE_FILLING, 400),
]

# Данные для параметризованных тестов чека
RECEIPT_TEST_DATA = [
    (
        "Белая булочка", 
        "Соус острый", 
        INGREDIENT_TYPE_SAUCE,
        "(==== Белая булочка ====)\n= sauce Соус острый =\n(==== Белая булочка ====)\n\nPrice: 250"
    ),
    (
        "Черная булочка", 
        "Котлета", 
        INGREDIENT_TYPE_FILLING,
        "(==== Черная булочка ====)\n= filling Котлета =\n(==== Черная булочка ====)\n\nPrice: 400"
    ),
]

# Ожидаемый чек для нескольких ингредиентов
EXPECTED_RECEIPT_MULTIPLE = [
    "(==== Белая булочка ====)",
    "= sauce Соус острый =",
    "= filling Котлета =", 
    "(==== Белая булочка ====)",
    "",
    "Price: 450"
]