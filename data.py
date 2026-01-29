import random

from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class DataBun:
    NAME_BUN = 'Хлебная'
    PRICE_BUN = 100
    DATA_BUNS_DATABASE = [("black bun", 100), ("white bun", 200), ("red bun", 300)]

class DataIngredient:
    @staticmethod
    def random_type_ingredient():
        type_ingredient = ['SAUCE', 'FILLING']
        return random.choice(type_ingredient)


    NAME_INGREDIENT = "Крабовое"
    PRICE_INGREDIENT = 200
    INGREDIENT = ['FILLING', 'Крабовое', 200]

    DATA_FILLING_DATABASE = [(INGREDIENT_TYPE_FILLING, "cutlet", 100),
                     (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
                     (INGREDIENT_TYPE_FILLING, "sausage", 300)]

    DATA_SAUCE_DATABASE = [(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
                           (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
                           (INGREDIENT_TYPE_SAUCE, "chili sauce", 300)]