class BurgerComponents:

    BUN_NAME_1 = "black bun"
    BUN_NAME_2 = "white bun"
    BUN_NAME_3 = "red bun"
    BUN_PRICE_1 = 100.0
    BUN_PRICE_2 = 200.0
    BUN_PRICE_3 = 300.0

    INGREDIENT_TYPE_1 = "SAUCE"
    SAUCE_NAME_1 = "hot sauce"
    SAUCE_NAME_2 = "sour cream"
    SAUCE_NAME_3 = "chili sauce"
    SAUCE_PRICE_1 = 100.0
    SAUCE_PRICE_2 = 200.0
    SAUCE_PRICE_3 = 300.0

    INGREDIENT_TYPE_2 = "FILLING"
    FILLING_NAME_1 = "cutlet"
    FILLING_NAME_2 = "dinosaur"
    FILLING_NAME_3 = "sausage"
    FILLING_PRICE_1 = 100.0
    FILLING_PRICE_2 = 200.0
    FILLING_PRICE_3 = 300.0

class IngredientIndex:

    FIRST_INGREDIENT = 0
    SECOND_INGREDIENT = 1
    THIRD_INGREDIENT = 2
    FOURTH_INGREDIENT = 3

class BurgerPrices:
    BURGER_PRICE_BLACK_BUNS = 100*2 # 200, бургер с двумя черными булочками
    BURGER_PRICE_BB_SC_D = 100*2 + 200 + 200 # 600, бургер с двумя чёрынми булочками, сметаной и динозавром
    BURGER_PRICE_BB_SC_HC_D_S = 100*2 + 200 + 300 + 200 + 300 # 1200, бургер с двумя черными булочками, сметаной, чили-соусом, динозавром и сосиской