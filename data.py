BUN_PARAMS = [
    ('Black bun', 100),
    ('White bun', 80.5),
    ('',0),
    ('Test', -20)
]

INGREDIENT_PARAMS = [
    ("SAUCE", "Hot sauce", 50),
    ("FILLING", "Cutlet", 100),
    ("SAUCE", "Sour cream", 200),
    ("", "Empty type", 0),
    ("FILLING", "", 50),
]

BURGER_BUN_NAME = 'Black Bun'
BURGER_BUN_PRICE = 100
INGREDIENT_TYPE_SAUCE = 'SAUCE'
INGREDIENT_TYPE_FILLING = 'FILLING'
INGREDIENT_FILLING_NAME = 'Cutlet'
INGREDIENT_SAUCE_NAME = 'Hot sauce'
INGREDIENT_FILLING_1_PRICE = 50
INGREDIENT_FILLING_2_PRICE = 30
INGREDIENT_SAUCE_PRICE = 25
BURGER_EXPECTED_TOTAL = 280
EXPECTED_RECEIPT = '(==== Black Bun ====)\n= filling Cutlet =\n(==== Black Bun ====)\n\nPrice: 250'