BUN_BLACK_NAME = "blackblack bun"
BUN_WHITE_NAME = "whitewhite bun"
BUN_PRICE = 150
INGREDIENT_TOMATO = "Tomato"
INGREDIENT_KETCHUP = "Ketchup"
RECEIPT_EXPECTED = (
        f"(==== {BUN_BLACK_NAME} ====)\n"
        f"= sauce {INGREDIENT_KETCHUP} =\n"
        f"(==== {BUN_BLACK_NAME} ====)\n\n"
        f"Price: {BUN_PRICE * 2 + 50}"
    )