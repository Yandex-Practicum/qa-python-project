from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class Burger1:
    bun_name = 'Краторная булка N-200i'
    bun_price = 1255.0
    sauce_type = INGREDIENT_TYPE_SAUCE
    sauce_name = 'Соус фирменный Space Sauce'
    sauce_price = 80.0
    filling_type = INGREDIENT_TYPE_FILLING
    filling_name = 'Биокотлета из марсианской Магнолии'
    filling_price = 424.0
    burger_final_cost = bun_price * 2 + sauce_price + filling_price

class DatabaseInfo:

    buns_database = [
        [0, "black bun", 100],
        [1, "white bun", 200],
        [2, "red bun", 300]
                        ]

    ingredients_database = [
        [0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100],
        [1, INGREDIENT_TYPE_SAUCE, "sour cream", 200],
        [2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300],
        [3, INGREDIENT_TYPE_FILLING, "cutlet", 100],
        [4, INGREDIENT_TYPE_FILLING, "dinosaur", 200],
        [5, INGREDIENT_TYPE_FILLING, "sausage", 300]
                         ]



