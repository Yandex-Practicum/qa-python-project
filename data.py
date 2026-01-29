# data.py
TEST_BUNS = [
    {'name': 'Бутафория', 'price': 60.0},
    {'name': 'Биг Спешиал', 'price': 120.0},
]

TEST_BURGER = [
    {'name': 'Гранд', 'price': 150.0},
]

TEST_ADD_INGREDIENTS = [
    {'name': 'Кетчуп', 'price': 5.99, 'ingredient_type': 'SAUCE'},
    {'name': 'Котлета', 'price': 10.99, 'ingredient_type': 'FILLING'}
]

TEST_REMOVE_INGREDIENTS = [
    {'ingredient_type': 'SAUCE', 'name': 'Чили', 'price': 5.0},
    {'ingredient_type': 'FILLING', 'name': 'Катлета', 'price': 10.0}
]

TEST_MOVE_INGREDIENTS = [
    {'ingredient_type': 'SAUCE', 'name': 'Майонез', 'price': 5.0},
    {'ingredient_type': 'FILLING', 'name': 'Катлета', 'price': 100.0},
    {'ingredient_type': 'SAUCE', 'name': 'Чили', 'price': 8.0}
]

TEST_RECEIPT_DATA = [
    {
        'bun_name': 'Булочка',
        'ingredient_name': 'Майонез',
        'ingredient_type': 'FILLING',
        'price': 10.99,
        'expected_receipt': (
            "(==== Булочка ====)\n"
            "= filling Майонез =\n"
            "(==== Булочка ====)\n"
            "\nPrice: 10.99"
        )
    }
]

TEST_AVAILABLE_INGREDIENTS = [
    {'name': 'Салат', 'ingredient_type': 'SAUCE', 'price': 5.0},
]

TEST_INGREDIENTS = [
    {'ingredient_type': 'SAUCE', 'name': 'Кетчуп', 'price': 5.99},
    {'ingredient_type': 'FILLING', 'name': 'Котлета', 'price': 10.99},
]
