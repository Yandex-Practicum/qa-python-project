from praktikum.ingredient_types import *
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class Data:
    Bun_name = 'Эльфийский хлеб'
    Bun_price = 1000

    Sauce_name = 'Еловый привкус Байкала'
    Sauce_price = 100
    Sauce_type = INGREDIENT_TYPE_SAUCE

    Filling_type = INGREDIENT_TYPE_FILLING
    Filling_name = 'Верблюжий горб'
    Filling_price = 300

    buns_data_for_test_database = [
                          [0, 'black bun', 100],
                          [1, "white bun", 200],
                          [2, "red bun", 300]
                                  ]
    ingredients_data_for_test_database = [
                    [0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100],
                    [1, INGREDIENT_TYPE_SAUCE, "sour cream", 200],
                    [2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300],
                    [3, INGREDIENT_TYPE_FILLING, "cutlet", 100],
                    [4, INGREDIENT_TYPE_FILLING, "dinosaur", 200],
                    [5, INGREDIENT_TYPE_FILLING, "sausage", 300]
                                         ]
