class Data:
    BUN_NAME = 'WhiteBun'
    BUN_PRICE = 100
    INGREDIENT_TYPE = 'sauce'
    INGREDIENT_NAME = 'cheese sause'
    INGREDIENT_PRICE = 50
    BURGER_PRICE = 250


class ExpectedResult:
    RECEIPT = "(==== WhiteBun ====)\n" \
                "= sauce cheese sause =\n" \
                "(==== WhiteBun ====)\n" \
                "\n" \
                "Price: 250"