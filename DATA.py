from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class Buns:
    BUNS = [("black bun", 100), ("white bun", 200)]
    WHITE_BUN = "white bun"
    BLACK_BUN = "black bun"
    RED_BUN = "red bun"


class Price:
    WHITE_BUN_PRICE = 200
    BLACK_BUN_PRICE = 100
    RED_BUN_PRICE = 300
    HOT_SAUCE = 100
    SOUR_CREAM = 200
    CHILI_SAUCE = 300
    CUTLET = 100
    DINOSAUR = 200
    SAUSAGE = 300


class Ingridients:
    HOT_SAUCE = "hot sauce"
    SOUR_CREAM = "sour cream"
    CHILI_SAUCE = "chili sauce"
    CUTLET = "cutlet"
    DINOSAUR = "dinosaur"
    SAUSAGE = "sausage"


class Database_fill:
    DATABASE_INGRIDIENT = [
        Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
        Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300),
    ]
    DATABASE_BUNS = [
        Bun("black bun", 100),
        Bun("white bun", 200),
        Bun("red bun", 300),
    ]


class Count:
    ZERO_TO_FIVE = [0, 1, 2, 3, 4, 5]
    ZERO_TO_TWO = [0, 1, 2]
