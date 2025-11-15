from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
BUN_NAME = "test"
BUN_PRICE = 13.37

INGREDIENT_NAME = "pickles"
INGREDIENT_PRICE = 12.34

AVAILABLE_BUNS_COUNT = 3
AVAILABLE_INGREDIENTS_COUNT = 6

TEST_BUN = Bun(BUN_NAME, BUN_PRICE)
BURGER_INGREDIENT1 = Ingredient(INGREDIENT_TYPE_SAUCE, "sauce", 12.0)
BURGER_INGREDIENT2 = Ingredient(INGREDIENT_TYPE_FILLING, "filling", 11.0)
