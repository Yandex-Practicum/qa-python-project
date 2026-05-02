from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

bun_data = {
    'name': 'Кунжутная булка',
    'price': 150  
}

ingredient_data = [
    [INGREDIENT_TYPE_FILLING, 'Котлета говяжья', 320],
    [INGREDIENT_TYPE_SAUCE, 'Чесночный соус', 80]
]

exception_receipt = '(==== Кунжутная булка ====)\n= filling Котлета говяжья =\n= sauce Чесночный соус =\n(==== Кунжутная булка ====)\n\nPrice: 700'