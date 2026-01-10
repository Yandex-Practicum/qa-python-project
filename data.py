from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

BUNS_DATA = [
    ("black bun", 100),
    ("white bun", 200),
    ("red bun", 300)
]

SAUCES_DATA = [
    ("hot sauce", 100, INGREDIENT_TYPE_SAUCE),
    ("sour cream", 200, INGREDIENT_TYPE_SAUCE),
    ("chili sauce", 300, INGREDIENT_TYPE_SAUCE)
]

FILLINGS_DATA = [
    ("cutlet", 100, INGREDIENT_TYPE_FILLING),
    ("dinosaur", 200, INGREDIENT_TYPE_FILLING),
    ("sausage", 300, INGREDIENT_TYPE_FILLING)
]

ALL_INGREDIENTS_DATA = SAUCES_DATA + FILLINGS_DATA

INGREDIENTS_TEST_DATA = [
    {
        "type": INGREDIENT_TYPE_SAUCE,
        "name": "Соус Spicy-X",
        "price": 90.0
    },
    {
        "type": INGREDIENT_TYPE_FILLING,
        "name": "Мясо бессмертных моллюсков Protostomia",
        "price": 1337.0
    }
]

EXPECTED_RECEIPT = (
    "(==== black bun ====)\n"
    "= sauce hot sauce =\n"
    "= filling cheese =\n"
    "(==== black bun ====)\n"
    "\n"
    "Price: 280"
)

VERIFICATION_NAME = 'Краторная булка'
VERIFICATION_PRICE = 125.50
