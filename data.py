from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDataIngredients:

    data_buns = [
        [0, 'black bun', 100],
        [1, 'white bun', 200],
        [2, 'red bun', 300]
    ]

    data_ingredients = [
        [0, INGREDIENT_TYPE_SAUCE, 'hot sauce', 100],
        [1, INGREDIENT_TYPE_SAUCE, 'sour cream', 200],
        [2, INGREDIENT_TYPE_SAUCE, 'chili sauce', 300],
        [3, INGREDIENT_TYPE_FILLING, 'cutlet', 100],
        [4, INGREDIENT_TYPE_FILLING, 'dinosaur', 200],
        [5, INGREDIENT_TYPE_FILLING, 'sausage', 300]
    ]


class TestBurgerData:

    bun_name = 'Флюоресцентная булка R2-D3'
    bun_price = 988

    sauce_name = 'Соус Spicy-X'
    sauce_price = 90
    sauce_type = INGREDIENT_TYPE_SAUCE

    filling_name = 'Говяжий метеорит (отбивная)'
    filling_price = 3000
    filling_type = INGREDIENT_TYPE_FILLING

    bun_name_2 = 'Краторная булка N-200i'
    bun_price_2 = 1255

    sauce_name_2 = 'Соус фирменный Space Sauce'
    sauce_price_2 = 80
    sauce_type_2 = INGREDIENT_TYPE_SAUCE

    filling_name_2 = 'Хрустящие минеральные кольца'
    filling_price_2 = 300
    filling_type_2 = INGREDIENT_TYPE_FILLING

    burger_total_price = bun_price * 2 + sauce_price + filling_price

