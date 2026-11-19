from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class BurgerData:
    BUN_NAME = 'Флюоресцентная булка R2-D3'
    BUN_PRICE = 988

    SAUCE_TYPE = INGREDIENT_TYPE_SAUCE
    SAUCE_NAME = 'Соус Spicy-X'
    SAUCE_PRICE = 90

    FILLING_TYPE = INGREDIENT_TYPE_FILLING
    FILLING_NAME = 'Говяжий метеорит'
    FILLING_PRICE = 3000

    PRICE_TEST_DATA = [
        (100, [], 200),
        (100, [50], 250),
        (200, [100, 300], 800),
        (150.5, [49.5, 100.0], 450.5),
    ]
