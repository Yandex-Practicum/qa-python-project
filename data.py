class MakeBurger:
    BUN_NAME = 'black bun'
    BUN_PRICE = 100.0
    BUN_NAME2 = 'white bun'
    BUN_PRICE2 = 200.0
    
    SAUSE_TYPE = 'SAUSE'
    SAUSE_NAME = 'chili sauce'
    SAUSE_PRICE = 300
    
    FILLING_TYPE = 'FILLING'
    FILLING_NAME = 'cutlet'
    FILLING_PRICE = 100.0
    
    INGREDIENT_PRICE = 150.0
    BURGER_PRICE = 500


class BurgerGetPrice:

    BUNS_SAUCE_FILLING_PRICE = 400          # булки и 2 ингредиента
    BUNS_PRICE               = 100          # только булки
    BUNS_SAUCE_PRICE         = 200          # булки и соус
    SAUCE_PRICE              = 100          # только соус без булок
    EMPTY_BURGER_PRICE       = 0            # "пустой" бургер - без булок и ингредиентов