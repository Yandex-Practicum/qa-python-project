from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class DataOne:
    BUN_NAME = 'Флюоресцентная булка R2-D3'
    BUN_PRICE = 988

    SAUCE_TYPE = INGREDIENT_TYPE_SAUCE
    SAUCE_NAME = 'Соус Spicy-X'
    SAUCE_PRICE = 90

    FILLING_TYPE = INGREDIENT_TYPE_FILLING
    FILLING_NAME = 'Мясо бессмертных моллюсков Protostomia'
    FILLING_PRICE = 1350

    BURGER_PRICE = BUN_PRICE * 2 + SAUCE_PRICE + FILLING_PRICE


class DataTwo:
    BUN_NAME = 'Краторная булка N-200i'
    BUN_PRICE = 1255

    SAUCE_TYPE = INGREDIENT_TYPE_SAUCE
    SAUCE_NAME = 'Соус с шипами Антарианского плоскоходца'
    SAUCE_PRICE = 88

    FILLING_TYPE = INGREDIENT_TYPE_FILLING
    FILLING_NAME = 'Сыр с астероидной плесенью'
    FILLING_PRICE = 4142

    BURGER_PRICE = BUN_PRICE * 2 + SAUCE_PRICE + FILLING_PRICE

class DataBase:
    database_buns = [
        [0, 'black bun', 100],
        [1, 'white bun', 200],
        [2, 'red bun', 300]
    ]

    database_ingredients = [
        [0, INGREDIENT_TYPE_SAUCE, 'hot sauce', 100],
        [1, INGREDIENT_TYPE_SAUCE, 'sour cream', 200],
        [2, INGREDIENT_TYPE_SAUCE, 'chili sauce', 300],
        [3, INGREDIENT_TYPE_FILLING, 'cutlet', 100],
        [4, INGREDIENT_TYPE_FILLING, 'dinosaur', 200],
        [5, INGREDIENT_TYPE_FILLING, 'sausage', 300]
    ]