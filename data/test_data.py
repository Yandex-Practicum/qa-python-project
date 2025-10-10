BURGER_PRICE_CASES = [

    ([("SAUCE", "hot sauce", 100.0), ("FILLING", "cutlet", 100.0)], 600.0),
    ([("FILLING", "dinosaur", 200.0), ("SAUCE", "sour cream", 200.0)], 800.0),
]


def build_expected_receipt(bun, ingredient, burger) -> str:

    expected_lines = [
        f'(==== {bun.get_name()} ====)',
        f'= {ingredient.get_type().lower()} {ingredient.get_name()} =',
        f'(==== {bun.get_name()} ====)\n',
        f'Price: {burger.get_price()}'
    ]
    return '\n'.join(expected_lines)

