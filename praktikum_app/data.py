from praktikum_app.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class Data:
    SAUCE_NAME = 'Кетчуп'
    BUN_NAME = 'Булочка'
    FILLING_NAME = 'Котлета'

    BUN_PRICE = 100
    SAUCE_PRICE = 50
    FILLING_PRICE = 200

    DATA = [
        [
            BUN_NAME, BUN_PRICE, INGREDIENT_TYPE_SAUCE, SAUCE_NAME, SAUCE_PRICE, INGREDIENT_TYPE_FILLING, FILLING_NAME,
            FILLING_PRICE
        ],
        [
            'Бублик', 50, 'Соус', 'Сырный', 100, 'Начинка', 'Стейк', 300
        ]
    ]
