from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


BUN = [
    ('black bun', 100), 
    ('white bun', 200), 
    ('red bun', 300)
]

BUN_WITH_INDEX = [
    (0, 'black bun', 100),
    (1, 'white bun', 200),
    (2, 'red bun', 300)
]

FILLING = [
    (INGREDIENT_TYPE_FILLING, "cutlet", 100),
    (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    (INGREDIENT_TYPE_FILLING, "sausage", 300),
]

SAUCE = [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
    (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
]
