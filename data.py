from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class Data1:
    bun_name = 'Флюоресцентная булка R2-D3'
    bun_price = 988

    sauce_type = INGREDIENT_TYPE_SAUCE
    sauce_name = 'Соус традиционный галактический'
    sauce_price = 15

    filling_type = INGREDIENT_TYPE_FILLING
    filling_name = 'Мясо бессмертных моллюсков Protostomia'
    filling_price = 1337

    burger_final_cost = bun_price * 2 + sauce_price + filling_price


class Data2:
    bun_name = 'Краторная булка N-200i'
    bun_price = 1255

    sauce_type = INGREDIENT_TYPE_SAUCE
    sauce_name = 'Соус с шипами Антарианского плоскоходца'
    sauce_price = 88

    filling_type = INGREDIENT_TYPE_FILLING
    filling_name = 'Сыр с астероидной плесенью'
    filling_price = 4142

    burger_final_cost = bun_price * 2 + sauce_price + filling_price


class TestDataBase:
    test_data_base_buns = [
        [0, 'black bun', 100],
        [1, 'white bun', 200],
        [2, 'red bun', 300]
    ]

    test_data_base_ingredients = [
        [0, INGREDIENT_TYPE_SAUCE, 'hot sauce', 100],
        [1, INGREDIENT_TYPE_SAUCE, 'sour cream', 200],
        [2, INGREDIENT_TYPE_SAUCE, 'chili sauce', 300],
        [3, INGREDIENT_TYPE_FILLING, 'cutlet', 100],
        [4, INGREDIENT_TYPE_FILLING, 'dinosaur', 200],
        [5, INGREDIENT_TYPE_FILLING, 'sausage', 300]

    ]
