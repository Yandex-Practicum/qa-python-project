class DataBun:
    BUN_NAME = "Космос"
    BUN_PRICE = 100
    LIST_BUN = [
        ("black bun", 100),
        ("white bun", 200),

    ]

class DataIngredient:
    INGREDIENT_TYPE_FILLING = "FILLING"
    INGREDIENT_TYPE_SAUCE = "SAUCE"
    INGREDIENT_NAME = "cutlet"
    INGREDIENT_PRICE = 250

class DataBurger:
    BUN_DATA = {
        "name": DataBun.BUN_NAME,
        "price": DataBun.BUN_PRICE
    }
    INGREDIENT_DATA_FILLING = {
        "ingredient_type": DataIngredient.INGREDIENT_TYPE_FILLING,
        "name": DataIngredient.INGREDIENT_NAME,
        "price": DataIngredient.INGREDIENT_PRICE
    }
    INGREDIENT_DATA_SAUCE = {
        "ingredient_type": DataIngredient.INGREDIENT_TYPE_SAUCE,
        "name": DataIngredient.INGREDIENT_NAME,
        "price": DataIngredient.INGREDIENT_PRICE
    }

    INGREDIENT_DATA_LIST = [
        INGREDIENT_DATA_FILLING,
        INGREDIENT_DATA_SAUCE
    ]
    BURGER_PRICE = DataIngredient.INGREDIENT_PRICE + DataBun.BUN_PRICE * 2
    BURGER_RECEIPT = (
        f"(==== {DataBun.BUN_NAME} ====)\n"
        f"= {DataIngredient.INGREDIENT_TYPE_SAUCE.lower()} {DataIngredient.INGREDIENT_NAME} =\n"
        f"(==== {DataBun.BUN_NAME} ====)\n\n"
        f"Price: {BURGER_PRICE}"
    )
