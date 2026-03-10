from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

BUNS_DATA = [
    {"name": "black bun", "price": 100},
    {"name": "white bun", "price": 200},
    {"name": "red bun", "price": 300},
    {"name": "sesame bun", "price": 150},
    {"name": "brioche", "price": 250}
]

INGREDIENTS_DATA = [
    {"type": INGREDIENT_TYPE_SAUCE, "name": "hot sauce", "price": 100},
    {"type": INGREDIENT_TYPE_SAUCE, "name": "sour cream", "price": 200},
    {"type": INGREDIENT_TYPE_SAUCE, "name": "chili sauce", "price": 300},
    {"type": INGREDIENT_TYPE_FILLING, "name": "cutlet", "price": 100},
    {"type": INGREDIENT_TYPE_FILLING, "name": "dinosaur", "price": 200},
    {"type": INGREDIENT_TYPE_FILLING, "name": "sausage", "price": 300},
    {"type": INGREDIENT_TYPE_SAUCE, "name": "cheese sauce", "price": 150},
    {"type": INGREDIENT_TYPE_FILLING, "name": "lettuce", "price": 50}
]

MOVE_INGREDIENT_DATA = [
    {"index": 0, "new_index": 1, "expected_order": [1, 0]},
    {"index": 1, "new_index": 0, "expected_order": [1, 0]},
    {"index": 0, "new_index": 0, "expected_order": [0, 1]}
]

REMOVE_INGREDIENT_DATA = [
    {"index_to_remove": 0, "expected_count": 1},
    {"index_to_remove": 1, "expected_count": 1}
]