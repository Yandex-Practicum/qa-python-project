from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

TEST_BUN_DATA = {
    "names": [
        ("black bun", "black bun"),
        ("булочка", "булочка"),
        ("a", "a"),
    ],
    "prices": [
        (300.0, 300.0),
        (350.50, 350.50),
        (2, 2),
    ]
}

TEST_INGREDIENT_DATA = {
    "types": [
        (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_SAUCE),
        (INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_FILLING),
    ],
    "names": [
        ("соус", "соус"),
        ("ingredient", "ingredient"),
    ],
    "prices": [
        (100.0, 100.0),
        (0, 0),
        (350.50, 350.50),
    ]
}

TEST_BUN = {
    "name": "Булочка с кунжутом",
    "price": 50.0
}
TEST_BUN_2 = {
    "name": "Космическая булочка",
    "price": 150.0
}

TEST_SAUCE =  {
        "type": INGREDIENT_TYPE_SAUCE,
        "name": "Кетчуп",
        "price": 20.0
    }
TEST_FILLING_1 =  {
        "type": INGREDIENT_TYPE_FILLING,
        "name": "Котлета гриль",
        "price": 150.0
    }

TEST_FILLING_2 =  {
        "type": INGREDIENT_TYPE_FILLING,
        "name": "Сыр",
        "price": 80.0
    }

RECEIPT_TEMPLATE = (
    "(==== {bun} ====)\n"
    "= sauce {sauce} =\n"
    "= filling {filling} =\n"
    "(==== {bun} ====)\n"
    "\n"
    "Price: {price}"
)
EXPECTED_BUNS = [
    Bun("black bun", 100),
    Bun("white bun", 200),
    Bun("red bun", 300)
]

EXPECTED_INGREDIENTS = [
    Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
    Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
    Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
    Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)
]