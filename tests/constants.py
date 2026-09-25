from praktikum.ingredient_types import (
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING,
)


BUN_BLACK_NAME = "black bun"
BUN_BLACK_PRICE = 100

BUN_WHITE_NAME = "white bun"
BUN_WHITE_PRICE = 200

BUN_RED_NAME = "red bun"
BUN_RED_PRICE = 300



INGREDIENT_HOT_SAUCE = ("hot sauce", 100, INGREDIENT_TYPE_SAUCE)
INGREDIENT_SOUR_CREAM = ("sour cream", 200, INGREDIENT_TYPE_SAUCE)
INGREDIENT_CHILI_SAUCE = ("chili sauce", 300, INGREDIENT_TYPE_SAUCE)
INGREDIENT_CUTLET = ("cutlet", 100, INGREDIENT_TYPE_FILLING)
INGREDIENT_DINOSAUR = ("dinosaur", 200, INGREDIENT_TYPE_FILLING)
INGREDIENT_SAUSAGE = ("sausage", 300, INGREDIENT_TYPE_FILLING)

ALL_INGREDIENTS = [
    INGREDIENT_HOT_SAUCE,
    INGREDIENT_SOUR_CREAM,
    INGREDIENT_CHILI_SAUCE,
    INGREDIENT_CUTLET,
    INGREDIENT_DINOSAUR,
    INGREDIENT_SAUSAGE,
]



# Пустой бургер с чёрной булочкой: цена = 100 * 2 = 200
RECEIPT_EMPTY_BLACK_BUN = (
    "(==== black bun ====)\n"
    "(==== black bun ====)\n"
    "\n"
    "Price: 200.0"
)

# Бургер с чёрной булочкой и соусом hot sauce (100 * 2 + 50 = 250)
RECEIPT_BLACK_BUN_WITH_SAUCE = (
    "(==== black bun ====)\n"
    "= sauce hot sauce =\n"
    "(==== black bun ====)\n"
    "\n"
    "Price: 250.0"
)



RECEIPT_LINE_BLACK_BUN = "(==== black bun ====)"
RECEIPT_LINE_SAUCE_HOT = "= sauce hot sauce ="
RECEIPT_LINE_FILLING_CUTLET = "= filling cutlet ="


BUNS_COUNT = 3
INGREDIENTS_COUNT = 6
SAUCES_COUNT = 3
FILLINGS_COUNT = 3