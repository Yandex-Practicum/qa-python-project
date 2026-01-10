from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class Data:

    BUN_NAME = 'first bun'
    BUN_PRICE = 100.01

    INGREDIENT_TYPE = INGREDIENT_TYPE_SAUCE
    INGREDIENT_NAME = 'space sauce-1'
    INGREDIENT_PRICE = 50.02

    BUN_NAME_MOCKED = 'neo bun'
    BUN_PRICE_MOCKED = 1000.33

    INGREDIENT_TYPE_MOCKED = INGREDIENT_TYPE_FILLING
    INGREDIENT_NAME_MOCKED = 'galaxy dust'
    INGREDIENT_PRICE_MOCKED = 55.55

    RECEIPT =  ('(==== neo bun ====)\n'
                '= filling galaxy dust =\n'
                '(==== neo bun ====)\n'
                '\n'
                f'Price: 2056.21')
