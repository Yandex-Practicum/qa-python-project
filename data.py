from practicum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


BUN_NAME = 'Флюоресцентная булка R2-D3'
BUN_PRICE = 988

INGREDIENT_NAME = 'Соус Spicy-X'
INGREDIENT_PRICE = 90

BURGER_PRICE = (BUN_PRICE* 2) + INGREDIENT_PRICE

BURGER_FULL_RECEIPT = ('(==== '+BUN_NAME+' ====)\n'
                       '= '+INGREDIENT_TYPE_SAUCE.lower()+' '+INGREDIENT_NAME+' =\n'
                       '(==== '+BUN_NAME+' ====)\n\n'
                       'Price: '+str(BURGER_PRICE))

BUNS_NAME_PRICE = [
        ["black bun", 100],
        ["white bun", 200],
        ["red bun", 300]]

INGREDIENTS_TYPE_NAME_PRICE = [
        [INGREDIENT_TYPE_SAUCE, "hot sauce", 100],
        [INGREDIENT_TYPE_SAUCE, "sour cream", 200],
        [INGREDIENT_TYPE_SAUCE, "chili sauce", 300],
        [INGREDIENT_TYPE_FILLING, "cutlet", 100],
        [INGREDIENT_TYPE_FILLING, "dinosaur", 200],
        [INGREDIENT_TYPE_FILLING, "sausage", 300]]