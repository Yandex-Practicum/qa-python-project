from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

BUN_CASES = (
    ("classic bun", 100),
    ("premium bun", 200.5),
)

INGREDIENT_CASES = (
    (INGREDIENT_TYPE_SAUCE, "spicy sauce", 50),
    (INGREDIENT_TYPE_FILLING, "beef patty", 150),
)

BURGER_BUN = ("test bun", 100)

BURGER_INGREDIENTS = (
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 30),
    (INGREDIENT_TYPE_FILLING, "cutlet", 120),
    (INGREDIENT_TYPE_SAUCE, "mayo", 25),
)

REMOVE_INGREDIENT_CASES = (
    (0, (1, 2)),
    (1, (0, 2)),
    (2, (0, 1)),
    (-1, (0, 1)),
)

MOVE_INGREDIENT_CASES = (
    (0, 2, (1, 2, 0)),
    (2, 0, (2, 0, 1)),
    (1, 1, (0, 1, 2)),
)

DATABASE_BUN_NAMES = ("black bun", "white bun", "red bun")
DATABASE_BUN_PRICES = (100, 200, 300)
DATABASE_INGREDIENT_COUNT = 6
DATABASE_SAUCE_COUNT = 3
DATABASE_FILLING_COUNT = 3
