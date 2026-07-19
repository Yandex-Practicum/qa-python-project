from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

SAMPLE_BUN = Bun("black bun", 100)

SAMPLE_INGREDIENTS = [
    Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
    Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
    Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
]

BURGER_PRICE_DATA = [
    # (bun_price, ingredient_prices, expected_total)
    (100, [], 200),
    (100, [100], 300),
    (100, [100, 200], 500),
    (200, [100, 200, 100], 800),
]

RECEIPT_DATA = [
    # (bun_name, [(type, name)], expected_receipt_fragment)
    ("black bun", [], "(==== black bun ====)"),
    ("white bun", [("SAUCE", "ketchup")], "= sauce ketchup ="),
]
