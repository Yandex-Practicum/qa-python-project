class TestData:

    INGREDIENT_CUTLLET_NAME = "cutlet"
    INGREDIENT_BLACK_BUN_NAME = "black bun"
    INGREDIENT_HOT_SAUCE_NAME = "hot sauce"
    INGREDIENT_TYPE_SAUCE = "SAUCE"
    INGREDIENT_TYPE_FILLING = "FILLING"
    CHEQUE_ORDER_TEXT_PRICE_BURGER_400 = "(==== black bun ====)\n= filling cutlet =\n= sauce hot sauce =\n(==== black bun ====)\n\nPrice: 400" # бургер ценой в 400 создается фикстурой с неизменяемой ценой(моки) - burger_two_ingredients_filling_sauce_bun