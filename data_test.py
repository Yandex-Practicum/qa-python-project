from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class BunConstants:
    BUN_NAME = "black bun"
    BUN_PRICE = 100


class IngredientConstants:
    SAUCE_TYPE = INGREDIENT_TYPE_SAUCE
    SAUCE_NAME = 'hot sauce'
    SAUCE_PRICE = 100
    FILLING_TYPE = INGREDIENT_TYPE_FILLING
    FILLING_NAME = 'dinosaur'
    FILLING_PRICE = 200
    TWO_SAME_INGREDIENTS = [[INGREDIENT_TYPE_SAUCE, 'hot sauce', 100], [INGREDIENT_TYPE_SAUCE, 'hot sauce', 100]]
    SAUCE_AND_FILLING = [[INGREDIENT_TYPE_SAUCE, 'hot sauce', 100], [INGREDIENT_TYPE_FILLING, 'cutlet', 100]]
    THREE_INGREDIENTS = [[INGREDIENT_TYPE_SAUCE, 'hot sauce', 100],
                         [INGREDIENT_TYPE_SAUCE, 'sour cream', 200],
                         [INGREDIENT_TYPE_FILLING, 'cutlet', 100]]


class Receipt:
    BURGER_RECEIPT = ("(==== black bun ====)\n"
                      "= filling dinosaur =\n"
                      "= sauce hot sauce =\n"
                      "(==== black bun ====)\n"
                      "\n"
                      "Price: 500")


class DatabaseList:
    BUN_LIST = [['black bun', 100, 0],
                ['white bun', 200, 1],
                ['red bun', 300, 2]]
    INGREDIENT_LIST = [[INGREDIENT_TYPE_SAUCE, 'hot sauce', 100, 0],
                       [INGREDIENT_TYPE_SAUCE, 'sour cream', 200, 1],
                       [INGREDIENT_TYPE_SAUCE, 'chili sauce', 300, 2],
                       [INGREDIENT_TYPE_FILLING, 'cutlet', 100, 3],
                       [INGREDIENT_TYPE_FILLING, 'dinosaur', 200, 4],
                       [INGREDIENT_TYPE_FILLING, 'sausage', 300, 5]]