from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class Data:
    BUN_NAME = 'Флюоресцентная булка R2-D3'
    PRICE_BUNS = 988

    SAUCES_TYPE = INGREDIENT_TYPE_SAUCE
    SAUCES_NAME = 'Соус фирменный Space Sauce'
    SAUCES_PRICE = 80

    FILLING_TYPE = INGREDIENT_TYPE_FILLING
    FILLING_NAME = 'Говяжий метеорит (отбивная)'
    FILLING_PRICE = 3000

    FINAL_VALUE_BURGER = PRICE_BUNS * 2 + SAUCES_PRICE + FILLING_PRICE


class Data_1:
    BUN_NAME = 'Краторная булка N-200i'
    PRICE_BUNS = 1255

    SAUCES_TYPE = INGREDIENT_TYPE_SAUCE
    SAUCES_NAME = 'Соус Spicy-X'
    SAUCES_PRICE = 90

    FILLING_TYPE = INGREDIENT_TYPE_FILLING
    FILLING_NAME = 'Мясо бессмертных моллюсков Protostomia'
    FILLING_PRICE = 1337

    FINAL_VALUE_BURGER = PRICE_BUNS * 2 + SAUCES_PRICE + FILLING_PRICE


class TestDataBase:

    TEST_BUN_FROM_DATABASE = [
        [0, 'black bun', 100],
        [1, 'white bun', 200],
        [2, 'red bun', 300]
    ]

    TEST_DATABASE_INGREDIENTS = [
        [0, INGREDIENT_TYPE_SAUCE, 'hot sauce', 100],
        [1, INGREDIENT_TYPE_SAUCE, 'sour cream', 200],
        [2, INGREDIENT_TYPE_SAUCE, 'chili sauce', 300],
        [3, INGREDIENT_TYPE_FILLING, 'cutlet', 100],
        [4, INGREDIENT_TYPE_FILLING, 'dinosaur', 200],
        [5, INGREDIENT_TYPE_FILLING, 'sausage', 300]

    ]
