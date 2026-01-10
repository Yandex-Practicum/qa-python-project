def buns_list():
    return [['black bun', 100],
            ['white bun', 200],
            ['red bun', 300],
            ['', 400],
            [500, False],
            [False, '600'],
            [700.7, 700.7]]


def ingredients_list():
    return [['sauce', 'hot sauce', 100],
            ['sauce', 'sour cream', 200],
            ['sauce', 'chili sauce', 300],
            ['filling', 'cutlet', 100],
            ['filling', 'dinosaur', 200],
            ['filling', 'sausage', 300],
            ['', '', ''],
            [False, False, False],
            [100.0, 100.0, 100.0]]


def first_ingredient():
    return ['sauce', 'hot sauce', 100]


def second_ingredient():
    return ['filling', 'sausage', 300]


def bun_test():
    return 'black bun', 100, 'black bun', 100


def ingredient_1_test():
    return 'sauce', 'hot sauce', 100, 'sauce', 'hot sauce', 100


def ingredient_2_test():
    return 'filling', 'sausage', 300, 'filling', 'sausage', 300


def price_test():
    return 600


def receipt_test():
    return '(==== black bun ====)\n= sauce hot sauce =\n= filling sausage =\n(==== black bun ====)\n\nPrice: 600'
