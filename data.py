from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


class Data:
    bun = {
        'name': 'Космо-булка',
        'price': 12.50
    }

    ingredient = {
        'type': INGREDIENT_TYPE_SAUCE,
        'name': 'Ворчестер',
        'price': 5.20
    }

    another_ingredient = {
        'type': INGREDIENT_TYPE_FILLING,
        'name': 'Говяжья котлета',
        'price': 25.70
    }

    get_receipt_params = {
        'bun_get_name': 'Булка',
        'ingredient_get_type': INGREDIENT_TYPE_SAUCE.lower(),
        'ingredient_get_name': 'Очень вкусный соус',
        'burger_get_price': '10.10'
    }
